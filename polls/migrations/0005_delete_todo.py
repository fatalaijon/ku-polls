# Generated by Django 3.1 on 2020-10-24 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_todo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todo',
        ),
    ]