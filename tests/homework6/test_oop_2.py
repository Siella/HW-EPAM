import datetime as dt
from unittest.mock import Mock

import pytest

from homework6.oop_2 import Homework, HomeworkResult, Student, Teacher


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


def test_homeworkresult_error():
    good_student = Student('Lev', 'Sokolov')
    with pytest.raises(Exception) as excinfo:
        HomeworkResult(good_student, "fff", "Solution")
    assert str(excinfo.value) == 'You gave not a Homework object'


def test_homework_done():
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')
    opp_teacher = Teacher('Daniil', 'Shadrin')
    good_student = Student('Lev', 'Sokolov')
    lazy_student = Student('Roman', 'Petrov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_3 = good_student.do_homework(oop_hw, 'I have done this hw again')
    result_4 = lazy_student.do_homework(docs_hw, 'done')
    result_5 = lazy_student.do_homework(docs_hw, 'done with efforts')

    opp_teacher.check_homework(result_1)
    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    advanced_python_teacher.check_homework(result_1)
    advanced_python_teacher.check_homework(result_4)
    advanced_python_teacher.check_homework(result_5)

    assert len(Teacher.homework_done[oop_hw]) == 2
    assert len(Teacher.homework_done.keys()) == 2

    Teacher.reset_results(oop_hw)

    assert len(Teacher.homework_done.keys()) == 1

    Teacher.reset_results()

    assert len(Teacher.homework_done.keys()) == 0
