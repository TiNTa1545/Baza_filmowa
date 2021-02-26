from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='First name')
    last_name = models.CharField(max_length=64, verbose_name='Last name')
    year_of_birth = models.DateField(null=True, verbose_name='Date of birth')

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Screenwriter(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='First name')
    last_name = models.CharField(max_length=64, verbose_name='Last name')
    year_of_birth = models.DateField(null=True, verbose_name='Date of birth')

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='First name')
    last_name = models.CharField(max_length=64, verbose_name='Last name')
    year_of_birth = models.DateField(null=True, verbose_name='Date of birth')

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Music(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='First name')
    last_name = models.CharField(max_length=64, verbose_name='Last name')
    year_of_birth = models.DateField(null=True, verbose_name='Date of birth')

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128, verbose_name='Title')
    year = models.DateField(null=False, verbose_name='World premiere date')
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL, verbose_name='Director')
    screenwriter = models.ForeignKey(Screenwriter, null=True, on_delete=models.SET_NULL, verbose_name='Screenwriter')
    music = models.ForeignKey(Music, null=True, on_delete=models.SET_NULL, verbose_name='Music')
    actors = models.ManyToManyField(Actor, verbose_name='Actors')

    @property
    def name(self):
        return "{} {}".format(self.title, self.year)

    def __str__(self):
        return self.name
