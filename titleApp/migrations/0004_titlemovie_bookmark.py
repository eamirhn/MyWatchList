# Generated by Django 3.2.7 on 2021-10-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titleApp', '0003_auto_20211003_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='titlemovie',
            name='bookmark',
            field=models.BooleanField(default=False),
        ),
    ]
