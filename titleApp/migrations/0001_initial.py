# Generated by Django 3.2.7 on 2021-10-03 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=350)),
                ('private', models.BooleanField(default=True)),
                ('theme', models.CharField(choices=[(1, 'default'), (2, 'Classic theme'), (3, 'Tv-shows theme'), (4, 'Anime theme'), (5, 'Tokyo Night theme'), (6, 'Romatic Theme'), (7, 'Bloody theme'), (8, 'Asian theme'), (9, 'Sad theme'), (10, 'Lonely theme')], max_length=2)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TitleMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_movie', models.CharField(max_length=200)),
                ('movieDB_id', models.IntegerField(blank=True)),
                ('imdb_id', models.IntegerField(blank=True)),
                ('watched', models.BooleanField(default=False)),
                ('date_added', models.DateField()),
                ('list_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='titleApp.lists')),
            ],
        ),
    ]