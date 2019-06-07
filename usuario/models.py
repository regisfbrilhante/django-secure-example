from django.db import models
from django.contrib import admin
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=10)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name