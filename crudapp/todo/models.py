from django.db import models

# Create your models here.
class Todo(models.Model):
    priority_options = {
        1:'urgent',
        2:'normal',
        3:'not important'
    }

    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(choices=priority_options)