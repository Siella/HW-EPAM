import sqlite3

import pytest
from oop_3.models import Homework, HomeworkResult, Student, Teacher


@pytest.mark.django_db
def test_db_population():
    s = Student(first_name='Test', last_name='Student')
    s.save()
    assert Student.objects.all().count() == 1

    t = Teacher(first_name='Test', last_name='Teacher')
    t.save()
    assert Teacher.objects.all().count() == 1

    t.create_homework('TEST task', 7)
    assert Homework.objects.all().count() == 1
    assert Homework.objects.all()[0].is_active() is True

    s.do_homework(1, 'TEST try')
    t.check_homework(1, 1)
    assert HomeworkResult.objects.filter(checked=1).count() == 1

    t.reset_results(hw_id=1)
    assert HomeworkResult.objects.all().count() == 0


def test_tables():
    with sqlite3.connect('homework12/db.sqlite3') as db:
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = list(map(lambda x: x[0], cursor.fetchall()))
    assert {'solutions', 'teachers', 'students', 'homeworks'} <= set(tables)
