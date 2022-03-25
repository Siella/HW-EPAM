"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime as dt
from collections import defaultdict


class Homework:
    """
    Homework принимает текст задания и дедлайн на его выполнение.
    :param text: текст задания
    :param deadline: число дней на выполнение
    :param created: точная дата и время создания
    """
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = dt.timedelta(deadline)
        self.created = dt.datetime.now()

    def is_active(self) -> bool:
        """
        Проверка на истечение срока выполнения ДЗ.
        :return: True, если задание не просрочено, иначе False
        """
        time_to_submit = self.created + self.deadline
        return time_to_submit - dt.datetime.now() > dt.timedelta(0)


class Person:
    """
    Человек с именем first_name и фамилией last_name.
    """
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class DeadlineError(Exception):
    pass


class Student(Person):
    def do_homework(self, homework: Homework, solution: str):
        """
        Выполение ДЗ.
        :param homework: какое ДЗ выполняется
        :param solution: решение ДЗ
        :return: HomeworkResult
        """
        if not homework.is_active():
            raise DeadlineError('You are late')
        return HomeworkResult(self, homework, solution)


class HomeworkResult:
    """
    HomeworkResult принимает объект автора задания, исходное задание
    и его решение в виде строки.
    :param homework: хранит объект Homework
    :param solution: хранит решение ДЗ как строку
    :param author: хранит объект Student
    :param created: c точной датой и временем создания
    """
    def __init__(self, author: Student, homework: Homework, solution: str):
        if not isinstance(homework, Homework):
            raise TypeError('You gave not a Homework object')
        self.homework = homework
        self.author = author
        self.solution = solution
        self.created = dt.datetime.now()


class Teacher(Person):
    """
    :param homework_done:
        сюда поподают все HomeworkResult после успешного прохождения
        check_homework, гарантировано остутствие повторяющихся результатов
        по каждому заданию, группировка по экземплярам Homework.
        Общий для всех учителей.
    :type homework_done: defaultdict
    """
    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """
        Создаёт ДЗ.
        :param text: тект задания
        :param deadline: срок исполнения
        :return: экземпляр Homework
        """
        return Homework(text, deadline)

    def check_homework(self, homework: HomeworkResult) -> bool:
        """
        Проверка результата выполения ДЗ студентом. Добавляет проверенную
        работу (при успешном выполнении) в общий пул с домашками.
        :param homework: экземпляр результата выполения ДЗ студентом
        :return: True, если число символов в решении > 5, иначе False.
        """
        if len(homework.solution) > 5:
            prev_solutions = [
                h.solution for h in self.homework_done[homework.homework]
            ]
            if homework.solution not in prev_solutions:
                self.homework_done[homework.homework].append(homework)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Homework = None) -> None:
        """
        Если передать экземпряр Homework, то удаляет только результаты
        этого задания из homework_done, если ничего не передавать,
        то полностью обнулит homework_done.
        :param homework: экземпряр Homework (default None)
        :return: None
        """
        if cls.homework_done[homework]:
            del cls.homework_done[homework]
        else:
            cls.homework_done.clear()


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
