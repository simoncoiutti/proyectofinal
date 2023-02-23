# Generated by Django 4.1.3 on 2023-01-27 13:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0014_alter_post_options_remove_post_estado_post_autor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='post',
            name='modificado',
        ),
        migrations.RemoveField(
            model_name='post',
            name='publicado',
        ),
        migrations.AddField(
            model_name='post',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Publicado/No Publicado'),
        ),
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Post', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(max_length=500, verbose_name='Bajada'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]