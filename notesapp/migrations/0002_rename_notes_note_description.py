# Generated by Django 4.0.4 on 2022-07-07 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='notes',
            new_name='description',
        ),
    ]