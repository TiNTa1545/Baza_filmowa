from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_login(login):
    """Walidator sprawdzający czy użytkownik o podanej nazwie istnieje już w bazie danych"""
    if User.objects.filter(username=login):
        raise ValidationError(message='User already exist in database!')
