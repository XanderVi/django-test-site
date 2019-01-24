from django.db import models
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_authenticated_user


'''
There are 3 groups of Users with different rights:
Full_rights: can do anything with Tasks and Categories
Usual_rights: can create task and change_task, but not delete
No_rights: can't do anything
'''


# Open or Closed tasks
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ("create_new_category", "Can create a new category"),
            ("delete_a_category", "Can delete category"),
            ("change_a_category", "Can change category"),
        )


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='all_tasks')
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True, name='date_published')
    deadline = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, default=get_current_authenticated_user,
                               on_delete=models.CASCADE,
                               related_name='author')
    worker = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='worker')

    def __str__(self):
        return self.title

    class Meta:
        permissions = (
            ("create_new_task", "Can create a new task"),
            ("delete_a_task", "Can delete task"),
            ("change_a_task", "Can change task"),
        )
