# Generated by Django 2.0.10 on 2019-01-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_auto_20190121_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
