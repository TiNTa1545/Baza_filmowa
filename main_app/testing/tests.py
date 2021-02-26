import pytest
from django.contrib.auth.models import User, Permission
from django.test import RequestFactory
from django.urls import resolve, reverse
from main_app.models import Actor, Director, Music, Screenwriter, Movie
from mixer.backend.django import mixer


@pytest.mark.parametrize("url", (
    'admin-panel',
    'index',
    'login',
    'add-user',
    'users-list',
    'my-profile',
    'change-password',
    'add-movie',
    'movies-list',
    'add-actor',
    'actors-list',
    'add-director',
    'directors-list',
    'add-music',
    'musics-list',
    'add-screenwriter',
    'screenwriters-list',
))
@pytest.mark.django_db
def test_urls(client, url, authorized_user):
    client.force_login(authorized_user)
    response = client.get(reverse(url))
    assert response.status_code == 200


@pytest.mark.django_db
def test_actor_add(client, authorized_user):
    client.force_login(authorized_user)
    response = client.post('/add_actor/', {'first_name': 'Franciszek', 'last_name': 'Jaki', 'year_of_birth': '1987-03-08'})
    assert response.status_code == 302
    assert len(Actor.objects.filter(first_name='Franciszek')) == 1


@pytest.mark.django_db
def test_actor_add2(client, unauthorized_user):
    client.force_login(unauthorized_user)
    response = client.post('/add_actor/', {'first_name': 'Franciszek', 'last_name': 'Jaki', 'year_of_birth': '1987-03-08'})
    assert response.status_code == 403


@pytest.mark.django_db
def test_screenwriter_add(client, authorized_user):
    client.force_login(authorized_user)
    response = client.post('/add_screenwriter/', {'first_name': 'Janina', 'last_name': 'Szwed', 'year_of_birth': '1977-07-11'})
    assert response.status_code == 302
    assert len(Screenwriter.objects.filter(first_name='Janina')) == 1


@pytest.mark.django_db
def test_screenwriter_add2(client, unauthorized_user):
    client.force_login(unauthorized_user)
    response = client.post('/add_screenwriter/', {'first_name': 'Janina', 'last_name': 'Szwed', 'year_of_birth': '1977-07-11'})
    assert response.status_code == 403


@pytest.mark.django_db
def test_music_add(client, authorized_user):
    client.force_login(authorized_user)
    response = client.post('/add_music/', {'first_name': 'Jacek', 'last_name': 'Wars', 'year_of_birth': '1922-12-22'})
    assert response.status_code == 302
    assert len(Music.objects.filter(first_name='Jacek')) == 1


@pytest.mark.django_db
def test_music_add2(client, unauthorized_user):
    client.force_login(unauthorized_user)
    response = client.post('/add_music/', {'first_name': 'Jacek', 'last_name': 'Wars', 'year_of_birth': '1922-12-22'})
    assert response.status_code == 403


@pytest.mark.django_db
def test_director_add(client, authorized_user):
    client.force_login(authorized_user)
    response = client.post('/add_director/', {'first_name': 'Anna', 'last_name': 'Druga', 'year_of_birth': '1944-01-12'})
    assert response.status_code == 302
    assert len(Director.objects.filter(first_name='Anna')) == 1


@pytest.mark.django_db
def test_director_add2(client, unauthorized_user):
    client.force_login(unauthorized_user)
    response = client.post('/add_director/', {'first_name': 'Anna', 'last_name': 'Druga', 'year_of_birth': '1944-01-12'})
    assert response.status_code == 403


@pytest.mark.django_db
def test_movie_add(client, authorized_user, test_movie, test_music, test_screenwriter, test_actor, test_director):
    client.force_login(authorized_user)
    response = client.post('/add_movie/', {'title': 'Pierwszy', 'director': test_director.id, 'music': test_music.id, 'screenwriter': test_screenwriter.id, 'year': '2012-11-01'})
    assert response.status_code == 200
    print(test_director.id)

