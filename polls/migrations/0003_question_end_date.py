# Generated by Django 3.1 on 2020-10-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201024_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(null=True, verbose_name='poll closing date'),
        ),
    ]
