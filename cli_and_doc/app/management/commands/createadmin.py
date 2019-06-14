from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import getpass


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = input('Username: ')
        email = input('Email address: ')
        password1 = getpass.getpass('Password: ')
        password2 = getpass.getpass('Password (again): ')
        while password1 != password2:
            password2 = getpass.getpass("Error: Your passwords didn't match. Try again: ")
        User.objects.create_superuser(username=username, email=email, password=password1)
        print('Superuser created successfully')