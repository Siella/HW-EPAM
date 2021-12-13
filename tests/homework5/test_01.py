import datetime as dt
from unittest.mock import Mock

from homework5.oop_1 import Homework, Student, Teacher


class FakeHomework(Homework):
    def __init__(self, text: str, deadline: int):
        super().__init__(text, deadline)
        self.created = dt.datetime(1996, 1, 1, 0, 0, 0)


def test_homework_expired(monkeypatch):
    datetime_mock = Mock(wrap=dt.datetime)
    datetime_mock.now.return_value = dt.datetime(1997, 1, 1, 0, 0, 0)
    homework = FakeHomework('expired task', 5)
    assert homework.is_active() is False


def test_active_homework():
    homework = Homework('do it', 5)
    assert homework.is_active() is True


def test_student_creation():
    student = Student('Roman', 'Petrov')
    assert student.first_name == 'Roman'
    assert student.last_name == 'Petrov'


def test_teacher_creation():
    teacher = Teacher('Roman', 'Petrov')
    assert teacher.first_name == 'Roman'
    assert teacher.last_name == 'Petrov'
