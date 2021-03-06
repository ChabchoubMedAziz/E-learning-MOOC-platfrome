# Generated by Django 3.2.7 on 2022-04-17 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='Is Student'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Is Teacher'),
        ),
    ]
