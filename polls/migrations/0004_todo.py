# Generated by Django 3.1 on 2020-10-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=80)),
                ('done', models.BooleanField(default=False, verbose_name='Description')),
            ],
        ),
    ]
