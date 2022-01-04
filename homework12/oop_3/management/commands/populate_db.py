from django.core.management.base import BaseCommand

from oop_3.models import Student, Teacher


class Command(BaseCommand):
    def _populate_all(self):
        s = Student(first_name='Egor', last_name='Shikov')
        s.save()

        t = Teacher(first_name='Petr', last_name='Basov')
        t.save()

        t.create_homework('OOP task', 7)
        s.do_homework(1, 'My first try')
        t.check_homework(1, 1)

    def handle(self, *args, **options):
        self._populate_all()
