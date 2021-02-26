from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, DeleteView

from main_app.forms import AddUserForm, LoginForm, UserModelForm, ScreenwriterModelForm, MusicModelForm, \
    DirectorModelForm, ActorModelForm, MovieModelForm, AddMovieForm, AddScreenwriterForm, AddMusicForm, AddDirectorForm, \
    AddActorForm
from main_app.models import Movie, Actor, Director, Music, Screenwriter


class BaseView(View):
    """Wyświetla widok strony głównej"""
    def get(self, request):
        return render(request, 'base.html')


@login_required
def admin_panel(request):
    """Wyświetla panel admina"""
    return render(request, 'admin_panel.html')


def django_admin_users(request):
    """Wyświetla panel django-admin"""
    return redirect(request, 'django-admin-user')


class LoginView(View):
    """Wyświetla widok strony logowania"""
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        received_form = LoginForm(request.POST)
        if received_form.is_valid():
            user = authenticate(username=received_form.cleaned_data['username'],
                                password=received_form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'form': received_form})
        else:
            return render(request, 'login.html', {'form': received_form})


class LogoutView(View):
    """Pozwala wylogować użytkownika"""
    def get(self, request):
        logout(request)
        return redirect('/')


class AddUserView(View):
    """Dodaje użytkownika do bazy"""
    def get(self, request):
        form = AddUserForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['login'],
                                     password=form.cleaned_data['password1'],
                                     email=form.cleaned_data['email'],
                                     first_name=form.cleaned_data['first_name'],
                                     last_name=form.cleaned_data['last_name'])
            return redirect('/login/')
        else:
            return render(request, 'add_user.html', {'form': form})


class MyProfileView(LoginRequiredMixin, View):
    """Wyświetla panel użytkownika"""
    def get(self, request):
        return render(request, 'my_profile.html')


class ChangePasswordView(LoginRequiredMixin, View):
    """Pozwala zmienić hasło użytkownika"""
    def get(self, request):
        return render(request, 'password_change.html')

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/logout')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'login.html', {'form': form})


class UsersListView(LoginRequiredMixin, View):
    """Wyświetla listę użytkowników"""
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users_list.html', {'users': users})


class UserDetailView(LoginRequiredMixin, View):
    """Wyświetla szczegółowe dane o użytkowniku"""
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'user_profile.html', {'user': user})


class AdminUserEditView(LoginRequiredMixin, View):
    """Pozwala adminowi edytować użytkownika"""
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        form = UserModelForm(instance=user)
        return render(request, 'admin_user_edit.html', {'form': form})

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        form = UserModelForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(f'/user_detail/{user.id}')
        else:
            return render(request, 'admin_user_edit.html', {'form': form})


class AddMovieView(PermissionRequiredMixin, LoginRequiredMixin, View):
    """Pozwala użytkownikom z odpowiednimi uprawnieniami dodać film do bazy"""
    permission_required = 'main_app.add_movie'

    def get(self, request):
        form = AddMovieForm()
        return render(request, 'add_movie.html', {'form': form})

    def post(self, request):
        form = AddMovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            director = form.cleaned_data['director']
            music = form.cleaned_data['music']
            screenwriter = form.cleaned_data['screenwriter']
            actors = form.cleaned_data['actors']
            m= Movie.objects.create(title=title, year=year, director=director, music=music, screenwriter=screenwriter)
            m.actors.set(actors)
            return redirect('/movies_list/')
        return render(request, 'add_movie.html', {'form': form})


class MoviesListView(LoginRequiredMixin, View):
    """Wyświetla listę filmów"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies_list.html', {'movies': movies})


class MovieDetailView(LoginRequiredMixin, View):
    """Wyświetla szczegółowe dane o filmie"""
    def get(self, request, movie_id):
        movies = Movie.objects.get(id=movie_id)
        return render(request, 'movie_details.html', {'movies': movies})


class UpdateMovieView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    """Pozwala na wprowadzanie zmian w filmach"""
    permission_required = 'main_app.change_movie'
    model = Movie
    fields = "__all__"
    template_name = "movie_details.html"
    success_url = '/movies_list/'


class DeleteMovieView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """Usuwa film"""
    permission_required = 'main_app.delete_movie'
    model = Movie
    template_name = "delete.html"
    success_url = '/movies_list/'


class AdminMovieEditView(LoginRequiredMixin, View):
    """Pozwala adminowi edytować film"""
    def get(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        form = MovieModelForm(instance=movie)
        return render(request, 'admin_edit.html', {'form': form})

    def post(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect(f'/movie_detail/{movie.id}')
        else:
            return render(request, 'admin_edit.html', {'form': form})


class AddActorView(PermissionRequiredMixin, LoginRequiredMixin, View):
    """Pozwala użytkownikom z odpowiednimi uprawnieniami dodać aktora do bazy"""
    permission_required = 'main_app.add_actor'
    def get(self, request):
        form = AddActorForm()
        return render(request, 'add_actor.html', {'form': form})

    def post(self, request):
        form = AddActorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            year = form.cleaned_data['year_of_birth']
            Actor.objects.create(first_name=first_name, last_name=last_name, year_of_birth=year)
            return redirect('/actors_list/')
        return render(request, 'add_actor.html', {'form': form})


class ActorsListView(LoginRequiredMixin, View):
    """Wyświetla listę aktorów"""
    def get(self, request):
        actors = Actor.objects.all()
        return render(request, 'actors_list.html', {'actors': actors})


class ActorDetailView(LoginRequiredMixin, View):
    """Wyświetla szczegółowe dane o aktorach"""
    def get(self, request, actor_id):
        actors = Actor.objects.get(id=actor_id)
        return render(request, 'actor_details.html', {'actors': actors})


class UpdateActorView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    """Pozwala na wprowadzanie zmian w aktorach"""
    permission_required = 'main_app.change_actor'
    model = Actor
    fields = "__all__"
    template_name = "actor_details.html"
    success_url = '/actors_list/'


class DeleteActorView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """Usuwa aktora"""
    permission_required = 'main_app.delete_actor'
    model = Actor
    template_name = "delete.html"
    success_url = '/actors_list/'


class AdminActorEditView(LoginRequiredMixin, View):
    """Pozwala adminowi edytować aktora"""
    def get(self, request, actor_id):
        actor = Actor.objects.get(id=actor_id)
        form = ActorModelForm(instance=actor)
        return render(request, 'admin_edit.html', {'form': form})

    def post(self, request, actor_id):
        actor = Actor.objects.get(id=actor_id)
        form = ActorModelForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect(f'/actor_detail/{actor.id}')
        else:
            return render(request, 'admin_edit.html', {'form': form})


class AddDirectorView(PermissionRequiredMixin, LoginRequiredMixin, View):
    """Pozwala użytkownikom z odpowiednimi uprawnieniami dodać reżysera do bazy"""
    permission_required = 'main_app.add_director'
    def get(self, request):
        form = AddDirectorForm()
        return render(request, 'add_director.html', {'form': form})

    def post(self, request):
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            year = form.cleaned_data['year_of_birth']
            Director.objects.create(first_name=first_name, last_name=last_name, year_of_birth=year)
            return redirect('/directors_list/')
        return render(request, 'add_director.html', {'form': form})


class DirectorsListView(LoginRequiredMixin, View):
    """Wyświetla listę reżyserów"""
    def get(self, request):
        directors = Director.objects.all()
        return render(request, 'directors_list.html', {'directors': directors})


class DirectorDetailView(LoginRequiredMixin, View):
    """Wyświetla szczegółowe dane o reżyserach"""
    def get(self, request, director_id):
        directors = Director.objects.get(id=director_id)
        return render(request, 'director_details.html', {'directors': directors})


class UpdateDirectorView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    """Pozwala na wprowadzanie zmian w reżyserach"""
    permission_required = 'main_app.change_director'
    model = Director
    fields = "__all__"
    template_name = "director_details.html"
    success_url = '/directors_list/'


class DeleteDirectorView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """Usuwa reżysera"""
    permission_required = 'main_app.delete_director'
    model = Director
    template_name = "delete.html"
    success_url = '/directors_list/'


class AdminDirectorEditView(LoginRequiredMixin, View):
    """Pozwala adminowi edytować reżysera"""
    def get(self, request, director_id):
        director = Director.objects.get(id=director_id)
        form = DirectorModelForm(instance=director)
        return render(request, 'admin_edit.html', {'form': form})

    def post(self, request, director_id):
        director = Director.objects.get(id=director_id)
        form = DirectorModelForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return redirect(f'/director_detail/{director.id}')
        else:
            return render(request, 'admin_edit.html', {'form': form})


class AddMusicView(PermissionRequiredMixin, LoginRequiredMixin, View):
    """Pozwala użytkownikom z odpowiednimi uprawnieniami dodać autora muzyki do bazy"""
    permission_required = 'main_app.add_music'
    def get(self, request):
        form = AddMusicForm()
        return render(request, 'add_music.html', {'form': form})

    def post(self, request):
        form = AddMusicForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            year = form.cleaned_data['year_of_birth']
            Music.objects.create(first_name=first_name, last_name=last_name, year_of_birth=year)
            return redirect('/musics_list/')
        return render(request, 'add_music.html', {'form': form})


class MusicsListView(LoginRequiredMixin, View):
    """Wyświetla listę autorów muzyki"""
    def get(self, request):
        musics = Music.objects.all()
        return render(request, 'musics_list.html', {'musics': musics})


class MusicDetailView(LoginRequiredMixin, View):
    """Wyświetla szczegółowe dane o autorze muzyki"""
    def get(self, request, music_id):
        musics = Music.objects.get(id=music_id)
        return render(request, 'music_details.html', {'musics': musics})


class UpdateMusicView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    """Pozwala na wprowadzanie zmian w autorach muzyki"""
    permission_required = 'main_app.change_music'
    model = Music
    fields = "__all__"
    template_name = "music_details.html"
    success_url = '/musics_list/'


class DeleteMusicView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """Usuwa autora muzyki"""
    permission_required = 'main_app.delete_music'
    model = Music
    template_name = "delete.html"
    success_url = '/music_list/'


class AdminMusicEditView(LoginRequiredMixin, View):
    """Pozwala adminowi edytować autora muzyki"""
    def get(self, request, music_id):
        music = Music.objects.get(id=music_id)
        form = MusicModelForm(instance=music)
        return render(request, 'admin_edit.html', {'form': form})

    def post(self, request, music_id):
        music = Music.objects.get(id=music_id)
        form = MusicModelForm(request.POST, instance=music)
        if form.is_valid():
            form.save()
            return redirect(f'/music_detail/{music.id}')
        else:
            return render(request, 'admin_edit.html', {'form': form})


class AddScreenwriterView(PermissionRequiredMixin, LoginRequiredMixin, View):
    """Pozwala użytkownikom z odpowiednimi uprawnieniami dodać autora scenariusza do bazy"""
    permission_required = 'main_app.add_screenwriter'
    def get(self, request):
        form = AddScreenwriterForm()
        return render(request, 'add_screenwriter.html', {'form': form})

    def post(self, request):
        form = AddScreenwriterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            year = form.cleaned_data['year_of_birth']
            Screenwriter.objects.create(first_name=first_name, last_name=last_name, year_of_birth=year)
            return redirect('/screenwriters_list/')
        return render(request, 'add_screenwriter.html', {'form': form})


class ScreenwritersListView(LoginRequiredMixin, View):
    """Wyświetla listę autorów scenariusza"""
    def get(self, request):
        screenwriters = Screenwriter.objects.all()
        return render(request, 'screenwriters_list.html', {'screenwriters': screenwriters})


class ScreenwriterDetailView(LoginRequiredMixin, View):
    """Wyświetla szczegółowe dane o autorze scenariusza"""
    def get(self, request, screenwriter_id):
        screenwriters = Screenwriter.objects.get(id=screenwriter_id)
        return render(request, 'screenwriter_details.html', {'screenwriters': screenwriters})


class UpdateScreenwriterView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    """Pozwala na wprowadzanie zmian w autorach scenariusza"""
    permission_required = 'main_app.change_screenwriter'
    model = Screenwriter
    fields = "__all__"
    template_name = "screenwriter_details.html"
    success_url = '/screenwriter_list/'


class DeleteScreenwriterView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    """Usuwa autora scenariusza"""
    permission_required = 'main_app.delete_screenwriter'
    model = Screenwriter
    template_name = "delete.html"
    success_url = '/screenwriter_list/'


class AdminScreenwriterEditView(LoginRequiredMixin, View):
    """Pozwala adminowi edytować autora scenariusza"""
    def get(self, request, screenwriter_id):
        screenwriter = Screenwriter.objects.get(id=screenwriter_id)
        form = ScreenwriterModelForm(instance=screenwriter)
        return render(request, 'admin_edit.html', {'form': form})

    def post(self, request, screenwriter_id):
        screenwriter = Screenwriter.objects.get(id=screenwriter_id)
        form = ScreenwriterModelForm(request.POST, instance=screenwriter)
        if form.is_valid():
            form.save()
            return redirect(f'/screenwriter_detail/{screenwriter.id}')
        else:
            return render(request, 'admin_edit.html', {'form': form})