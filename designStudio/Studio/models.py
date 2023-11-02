from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class AdvUser(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)

    def full_name(self):
        # return self.name + ' ' + self.surname + ' ' + self.patronymic
        return ' '.join([self.name, self.surname, self.patronymic])

    def __str__(self):
        return self.full_name()


class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Введите категорию")

    def __str__(self):
        return self.name


class Application(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default='description')
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
