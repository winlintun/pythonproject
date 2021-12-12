from django.db import models
from datetime import datetime


class Tutorial(models.Model):
    title = models.CharField(max_length=200, help_text="Tutorial Title")
    content = models.TextField(help_text="Tutorial content")
    published = models.DateTimeField(default=datetime.now)
