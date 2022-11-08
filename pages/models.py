from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):

    name = models.CharField(max_length=50, help_text="Digite seu nome completo")
    photo = models.ImageField(upload_to='static/uploads/')

    def __str__(self):
        return self.name + ' - ' + str(self.photo)