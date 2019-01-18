from django.db import models
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_authenticated_user


#Open or Closed tasks
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='all_tasks')
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True, name='date published')
    deadline = models.DateTimeField()
    author = models.ForeignKey(User, default=get_current_authenticated_user,
                               on_delete=models.CASCADE,
                               related_name='author')
    worker = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='assigned_to')

    def __str__(self):
        return self.title
