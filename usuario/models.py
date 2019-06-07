from django.db import models

# Create your models here.


class Usuario(models.Model):
    name = models.CharField(max_length=10)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name