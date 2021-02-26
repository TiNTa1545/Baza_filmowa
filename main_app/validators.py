from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_login(login):
    if User.objects.filter(username=login):
        raise ValidationError(message='User already exist in database!')
