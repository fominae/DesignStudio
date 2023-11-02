from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Введите категорию")
    def __str__(self):
        return self.name
class Application(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default= 'description')
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title