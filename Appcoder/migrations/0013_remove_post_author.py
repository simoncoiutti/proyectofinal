# Generated by Django 4.1.3 on 2023-01-27 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0012_remove_usuario_profesion_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]