import django.forms as forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from main_app.models import Movie, Director, Actor, Screenwriter, Music
from main_app.validators import validate_login


class LoginForm(forms.Form):
    """Formularz logowania"""
    username = forms.CharField(max_length=64, label="Login")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


class AddUserForm(forms.Form):
    """Formularz dodawania nowego użytkownika"""
    login = forms.CharField(max_length=64, label="Login", validators=[validate_login])
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat password")
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='E-mail', validators=[EmailValidator])

    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise ValidationError(message='Please enter the same password in both password fields.')
        else:
            return data


class UserModelForm(forms.ModelForm):
    """Formularz pozwalający adminowi edytować użytkowników"""
    class Meta:
        model = User
        exclude = ['is_superuser', 'groups', 'last_login', 'date_joined', 'password', 'user_permissions']


class ActorModelForm(forms.ModelForm):
    """Formularz pozwalający adminowi dodawać/edytować aktorów"""
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorModelForm(forms.ModelForm):
    """Formularz pozwalający adminowi dodawać/edytować reżysera"""
    class Meta:
        model = Director
        fields = '__all__'


class MusicModelForm(forms.ModelForm):
    """Formularz pozwalający adminowi dodawać/edytować autora muzyki"""
    class Meta:
        model = Music
        fields = '__all__'


class ScreenwriterModelForm(forms.ModelForm):
    """Formularz pozwalający adminowi dodawać/edytować autora scenariusza"""
    class Meta:
        model = Screenwriter
        fields = '__all__'


class MovieModelForm(forms.ModelForm):
    """Formularz pozwalający adminowi dodawać/edytować film"""
    class Meta:
        model = Movie
        fields = '__all__'


class AddMovieForm(forms.Form):
    """Formularz dodawania nowego filmu"""
    directors = Director.objects.all()
    screenwriters = Screenwriter.objects.all()
    actors = Actor.objects.all()
    musics = Music.objects.all()
    title = forms.CharField(max_length=128, label="Title")
    year = forms.DateField(required=True, label='World premiere date', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    director = forms.ModelChoiceField(queryset=directors, label='Director')
    screenwriter = forms.ModelChoiceField(queryset=screenwriters, label='Screenwriter')
    music = forms.ModelChoiceField(queryset=musics, label='Music')
    actors = forms.ModelMultipleChoiceField(queryset=actors, label='Actors', widget=forms.widgets.CheckboxSelectMultiple)


class AddDirectorForm(forms.ModelForm):
    """Formularz dodawania nowego reżysera"""
    class Meta:
        model = Director
        fields = ['first_name', 'last_name', 'year_of_birth']
        widgets = {
            'year_of_birth': forms.DateInput(format='%d/%m/%Y',
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }


class AddActorForm(forms.ModelForm):
    """Formularz dodawania nowego aktora"""
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'year_of_birth']
        widgets = {
            'year_of_birth': forms.DateInput(format='%m/%d/%Y',
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }


class AddScreenwriterForm(forms.ModelForm):
    """Formularz dodawania nowego scenarzysty"""
    class Meta:
        model = Screenwriter
        fields = ['first_name', 'last_name', 'year_of_birth']
        widgets = {
            'year_of_birth': forms.DateInput(format='%m/%d/%Y',
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }


class AddMusicForm(forms.ModelForm):
    """Formularz dodawania nowego autora muzyki"""
    class Meta:
        model = Music
        fields = ['first_name', 'last_name', 'year_of_birth']
        widgets = {
            'year_of_birth': forms.DateInput(format='%m/%d/%Y',
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }
