# Generated by Django 3.1.6 on 2021-02-23 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='First name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last name')),
                ('year_of_birth', models.DateField(null=True, verbose_name='Year of birth')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='First name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last name')),
                ('year_of_birth', models.DateField(null=True, verbose_name='Year of birth')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='First name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last name')),
                ('year_of_birth', models.DateField(null=True, verbose_name='Year of birth')),
            ],
        ),
        migrations.CreateModel(
            name='Screenwriter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='First name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last name')),
                ('year_of_birth', models.DateField(null=True, verbose_name='Year of birth')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(verbose_name='Year of production')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.director', verbose_name='Director')),
                ('main_actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.actor', verbose_name='Main actor')),
                ('music', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.music', verbose_name='Music')),
                ('screenwriter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.screenwriter', verbose_name='Screenwriter')),
            ],
        ),
    ]
