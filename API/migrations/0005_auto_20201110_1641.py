# Generated by Django 3.1.3 on 2020-11-10 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20201109_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedata',
            old_name='imdbID',
            new_name='imdbid',
        ),
        migrations.RenameField(
            model_name='moviedata',
            old_name='relased',
            new_name='released',
        ),
    ]
