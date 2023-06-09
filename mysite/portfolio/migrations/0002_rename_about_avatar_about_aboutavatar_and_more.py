# Generated by Django 4.1.7 on 2023-03-31 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about_avatar',
            new_name='aboutAvatar',
        ),
        migrations.RenameField(
            model_name='myinfo',
            old_name='full_name',
            new_name='fullName',
        ),
        migrations.RenameField(
            model_name='myinfo',
            old_name='mini_describe',
            new_name='miniDescribe',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='skill',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='myinfo',
            name='mycv',
        ),
    ]
