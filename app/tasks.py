import string
from django.contrib.auth.models import User
from celery import shared_task
from django.utils.crypto import get_random_string

from celery_project.celery import app

@app.task
def create_random_user_accounts(total):
    print("In CELERY: ", total)
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)