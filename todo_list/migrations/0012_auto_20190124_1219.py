# Generated by Django 2.0.10 on 2019-01-24 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0011_auto_20190124_0824'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'permissions': (('create_new_category', 'Can create a new category'), ('delete_a_category', 'Can delete category'), ('change_a_category', 'Can change category'))},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('create_new_task', 'Can create a new task'), ('delete_a_task', 'Can delete task'), ('change_a_task', 'Can change task'))},
        ),
    ]
