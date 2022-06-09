from datetime import date, time

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone as tz
from django.utils.timezone import now

from base.models import Task


class TaskTestCase(TestCase):
    fixtures = ["group.json", "taks.json"]

    def setUp(self):
        Task.objects.create(title="Сдать 3 лабу по ИСП", description="Хочу допуск",
                            date=date.today(),
                            active=True
                            )

    def test_task(self):
        task1 = Task.objects.get(title="Сдать 3 лабу по ИСП")
        self.assertEqual(task1.description, "Хочу допуск")
        self.assertEqual(task1.date, date.today())
        self.assertEqual(task1.active, True)

    def test_get_user(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, "artem")

    def test_get_task(self):
        task = Task.objects.get(pk=8)
        self.assertEqual(task.title, "wash the dishes")

    def test_should_create_user_with_username(db) -> None:
        user = User.objects.create_user("Haki")
        assert user.username == "Haki"

    def test_should_check_password(db) -> None:
        user = User.objects.create_user("A")
        user.set_password("secret")
        assert user.check_password("secret") is True

    def test_should_not_check_unusable_password(db) -> None:
        user = User.objects.create_user("A")
        user.set_password("secret")
        user.set_unusable_password()
        assert user.check_password("secret") is False

