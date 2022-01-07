import datetime as dt

from django.db import models
from django.utils import timezone

MIN_SOLUTION_LEN = 5


class Homework(models.Model):
    text = models.TextField('текст задания')
    deadline = models.IntegerField('число дней на выполение задания')
    created = models.DateTimeField('когда создано задание')

    class Meta:
        db_table = 'homeworks'

    def __str__(self):
        return self.text

    def is_active(self):
        """
        Проверка на истечение срока выполнения ДЗ.

        :return: True, если задание не просрочено, иначе False
        """
        date_to_submit = self.created + dt.timedelta(days=self.deadline)
        return date_to_submit - timezone.now() > dt.timedelta(0)


class HomeworkResult(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, null=True)
    solver = models.ForeignKey('Student', on_delete=models.CASCADE, null=True)
    solution = models.TextField('решение задания')
    created = models.DateTimeField('время сдачи дз')
    checked = models.BooleanField('проверено ли дз', default=False)
    reviewer = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'solutions'

    def __str__(self):
        return f"{self.homework.text}, {self.solver.last_name}"


class DeadlineError(Exception):
    pass


class Person(models.Model):
    first_name = models.CharField('имя', max_length=100)
    last_name = models.CharField('фамилия', max_length=100)

    class Meta:
        abstract = True


class Student(Person):

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f"{self.last_name}"

    def do_homework(self, hw_id: int, solution: str):
        """
        Выполение ДЗ и запись результата в таблицу solutions.

        :param hw_id: id ДЗ из таблицы homeworks, которое выполняется
        :type hw_id: int
        :param solution: решение ДЗ
        :type solution: str
        """
        if not Homework.objects.get(id=hw_id).is_active():
            raise DeadlineError('You are late')
        HomeworkResult.objects.create(
            homework_id=hw_id, solver_id=self.id,
            solution=solution, created=timezone.now()
        )


class Teacher(Person):

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f"{self.last_name}"

    @staticmethod
    def create_homework(text: str, deadline: dt.datetime):
        """
        Создаёт ДЗ в таблице homeworks.

        :param text: тект задания
        :type text: str
        :param deadline: срок исполнения
        :type deadline: dt.datetime
        """
        Homework.objects.create(
            text=text, deadline=deadline, created=timezone.now()
        )

    def check_homework(self, hw_id: int, st_id: int):
        """
        Проверка результата выполения ДЗ студентом. Отмечает проверенную
        работу (при успешном выполнении) в отаблице solutions.

        :param hw_id: id ДЗ
        :type hw_id: int
        :param st_id: id студента, выполневшего ДЗ
        :type st_id: int
        """
        hw = HomeworkResult.objects.filter(
            homework_id=hw_id, solver_id=st_id
        ).latest('id')
        if len(hw.solution) > MIN_SOLUTION_LEN:
            hw.checked = 1
        hw.reviewer_id = self.id
        hw.save()

    @staticmethod
    def reset_results(hw_id: int = None):
        """
        Если передать id ДЗ, то удаляет только результаты
        этого задания из таблицы solutions.
        Если ничего не передавать, то полностью обнулит solutions.

        :param hw_id: id ДЗ
        :type hw_id: int
        """
        hw = HomeworkResult.objects.all()
        if hw_id is not None:
            hw = HomeworkResult.objects.filter(homework_id=hw_id)
        hw.delete()
