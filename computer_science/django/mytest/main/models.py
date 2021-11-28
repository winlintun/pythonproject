from django.db import models

# Create your models here.

class Todo(models.Model):
    content = models.TextField()

class Done(models.Model):
    content = models.ForeignKey(Todo, on_delete=models.CASCADE)
    done = models.CharField(max_length=6)
