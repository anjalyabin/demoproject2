# Generated by Django 2.2 on 2023-08-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1989-03-17'),
            preserve_default=False,
        ),
    ]
