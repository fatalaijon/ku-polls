# Generated by Django 3.1 on 2020-11-06 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_vote_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='question',
        ),
    ]
