"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime as dt


class Homework:
    """
    Homework принимает текст задания и дедлайн на его выполнение.

    :param text: текст задания
    :type text: str
    :param deadline: число дней на выполнение
    :type deadline: int
    :param created: точная дата и время создания
    :type created: datetime.datetime
    """
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = dt.timedelta(deadline)
        self.created = dt.datetime.now()

    def is_active(self) -> bool:
        """
        Проверка актуальности ДЗ.

        :return: Возвращает True, если ДЗ не просрочено,
            иначе False.
        :rtype: bool
        """
        now = dt.datetime.now()
        return self.created + self.deadline - now > dt.timedelta(0)


class Student:
    """
    Создаёт студента.

    :param first_name: имя
    :type first_name: str
    :param last_name: фамилия
    :type last_name: str
    """
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework: Homework) -> Homework:
        """
        Выполение ДЗ.

        :param homework: какое ДЗ выполняется
        :type homework: Homework
        :return: то же самое ДЗ, если оно не просрочено.
        :rtype: Homework(, None)
        """
        if homework.is_active():
            return homework
        print('You are late')


class Teacher:
    """
    Создаёт учителя.

    :param first_name: имя
    :type first_name: str
    :param last_name: фамилия
    :type last_name: str
    """
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """
        Создаёт ДЗ.

        :param text: тект задания
        :type text: str
        :param deadline: срок исполнения (в днях)
        :type deadline: int
        :return: ДЗ
        :rtype: Homework
        """
        return Homework(text, deadline)


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    print(teacher.last_name)  # Shadrin
    print(student.first_name)  # Roman

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
