# Generated by Django 2.0.10 on 2019-01-18 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_auto_20190118_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(default=django_currentuser.middleware.get_current_authenticated_user, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
