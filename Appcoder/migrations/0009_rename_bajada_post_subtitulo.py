# Generated by Django 4.1.3 on 2023-01-22 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0008_alter_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='bajada',
            new_name='subtitulo',
        ),
    ]
