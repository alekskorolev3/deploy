from datetime import date

from django.contrib.auth.models import User

from .models import Task
from asgiref.sync import sync_to_async


@sync_to_async()
def get_all_tasks():
    return Task.objects.all()


@sync_to_async()
def get_all_users():
    return User.objects.all()


@sync_to_async()
def get_all_today_tasks():
    return Task.objects.filter(date=date.today())
