# Generated by Django 4.2 on 2023-04-03 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='featured',
            new_name='destacado',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='ingredientes',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
    ]
