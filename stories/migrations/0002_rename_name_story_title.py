# Generated by Django 4.2.5 on 2023-10-17 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='name',
            new_name='title',
        ),
    ]
