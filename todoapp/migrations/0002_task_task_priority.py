# Generated by Django 3.1 on 2020-09-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_priority',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
    ]