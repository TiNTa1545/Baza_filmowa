"""Baza_filmowa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main_app.views import BaseView, LoginView, LogoutView, AddUserView, MyProfileView, ChangePasswordView, \
    UsersListView, UserDetailView, MoviesListView, MovieDetailView, ActorsListView, DirectorsListView, \
    DirectorDetailView, MusicDetailView, MusicsListView, ScreenwritersListView, ScreenwriterDetailView, \
    DeleteMovieView, DeleteActorView, DeleteDirectorView, DeleteMusicView, DeleteScreenwriterView, admin_panel, \
    AdminUserEditView, AdminMovieEditView, AdminActorEditView, AdminDirectorEditView, AdminMusicEditView, \
    AdminScreenwriterEditView, AddMovieView, AddActorView, AddDirectorView, AddMusicView, AddScreenwriterView, \
    ActorDetailView, django_admin_users

urlpatterns = [
    path('admin/', admin.site.urls, name='django-admin'),
    path('admin/auth/user/', django_admin_users, name='django-admin-user'),
    path('', BaseView.as_view(), name='index'),
    path('admin_panel/', admin_panel, name='admin-panel'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_user/', AddUserView.as_view(), name='add-user'),
    path('users_list/', UsersListView.as_view(), name='users-list'),
    path('user_detail/<int:user_id>', UserDetailView.as_view(), name='user-detail'),
    path('admin_user_edit/<int:user_id>', AdminUserEditView.as_view(), name='admin-user-edit'),
    path('my_profile/', MyProfileView.as_view(), name='my-profile'),
    path('password_change/', ChangePasswordView.as_view(), name='change-password'),
    path('add_movie/', AddMovieView.as_view(), name='add-movie'),
    path('movies_list/', MoviesListView.as_view(), name='movies-list'),
    path('movie_detail/<int:movie_id>', MovieDetailView.as_view(), name='movie-detail'),
    path("delete_movie/<int:pk>/", DeleteMovieView.as_view(), name='movie-delete'),
    path('admin_movie_edit/<int:movie_id>', AdminMovieEditView.as_view(), name='admin-movie-edit'),
    path('add_actor/', AddActorView.as_view(), name='add-actor'),
    path('actors_list/', ActorsListView.as_view(), name='actors-list'),
    path('actor_detail/<int:actor_id>', ActorDetailView.as_view(), name='actor-detail'),
    path("delete_actor/<int:pk>/", DeleteActorView.as_view(), name='actor-delete'),
    path('admin_actor_edit/<int:actor_id>', AdminActorEditView.as_view(), name='admin-actor-edit'),
    path('add_director/', AddDirectorView.as_view(), name='add-director'),
    path('directors_list/', DirectorsListView.as_view(), name='directors-list'),
    path('director_detail/<int:director_id>', DirectorDetailView.as_view(), name='director-detail'),
    path("delete_director/<int:pk>/", DeleteDirectorView.as_view(), name='director-delete'),
    path('admin_director_edit/<int:director_id>', AdminDirectorEditView.as_view(), name='admin-director-edit'),
    path('add_music/', AddMusicView.as_view(), name='add-music'),
    path('musics_list/', MusicsListView.as_view(), name='musics-list'),
    path('music_detail/<int:music_id>', MusicDetailView.as_view(), name='music-detail'),
    path("delete_music/<int:pk>/", DeleteMusicView.as_view(), name='music-delete'),
    path('admin_music_edit/<int:music_id>', AdminMusicEditView.as_view(), name='admin-music-edit'),
    path('add_screenwriter/', AddScreenwriterView.as_view(), name='add-screenwriter'),
    path('screenwriters_list/', ScreenwritersListView.as_view(), name='screenwriters-list'),
    path('screenwriter_detail/<int:screenwriter_id>', ScreenwriterDetailView.as_view(), name='screenwriter-detail'),
    path("delete_screenwriter/<int:pk>/", DeleteScreenwriterView.as_view(), name='screenwriter-delete'),
    path('admin_screenwriter_edit/<int:screenwriter_id>', AdminScreenwriterEditView.as_view(), name='admin-screenwriter-edit'),
]
