from django.contrib.auth.models import User, Permission
import pytest

from main_app.models import Actor, Director, Music, Screenwriter, Movie


@pytest.fixture
def unauthorized_user():
    unauthorized_user = User.objects.create_user(username='Jacek')
    return unauthorized_user


@pytest.fixture
def authorized_user():
    authorized_user = User.objects.create_user(username='Piotr')
    perm = Permission.objects.filter(codename__in=('add_movie', 'add_director', 'add_actor', 'add_music', 'add_screenwriter'))
    authorized_user.user_permissions.set(perm)
    return authorized_user


@pytest.fixture
def test_actor():
    actor = Actor.objects.create(first_name='Franciszek', last_name='Jaki', year_of_birth='1987-03-08')
    return actor


@pytest.fixture
def test_director():
    director = Director.objects.create(first_name='Anna', last_name='Druga', year_of_birth='1944-01-12')
    return director


@pytest.fixture
def test_music():
    music = Music.objects.create(first_name='Jacek', last_name='Wars', year_of_birth='1922-12-22')
    return music


@pytest.fixture
def test_screenwriter():
    screenwriter = Screenwriter.objects.create(first_name='Janina', last_name='Szwed', year_of_birth='1977-07-11')
    return screenwriter


@pytest.fixture
def test_movie():
    movie = Movie.objects.create(title='Pierwszy', year='2012-11-01', director_id='1', music_id='1', screenwriter_id='1')
    return movie

