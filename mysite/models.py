from django.contrib.auth.models import User
from django.db import models

class Graphic(models.Model):
    image = models.ImageField()
    title = models.TextField(max_length=20)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.TextField(max_length=40)

    def __str__(self):
        return self.title
    