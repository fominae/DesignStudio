from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from datetime import datetime


# Create your models here.
class AdvUser(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='ФИО', blank=False)


class Category(models.Model):
    category = models.CharField(
        verbose_name="Категория", unique=True)

    def __str__(self):
        return self.category


class Application(models.Model):
    application_title = models.CharField(max_length=254, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    REQUEST_CATEGORY = (
        ('bigApartment', 'bigApartment'),
        ('Medium-sizedApartment', 'Medium-sizedApartment'),
        ('smallApartment', 'smallApartment'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    photo_of_room = models.ImageField(max_length=254, upload_to="media/", verbose_name="Фотография",
                                      help_text="Разрешается формата файла только jpg, jpeg, png, bmp",
                                      validators=[
                                          FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']),
                                          validate_image])
    date_create = models.DateField(default=datetime.now, verbose_name="Дата создания")
    time_create = models.TimeField(default=datetime.now, verbose_name="Время создания")
    REQUEST_STATUS = (
        ('Новая', 'Новая'),
        ('Принято в работу', 'Принято в работу'),
        ('Выполнено', 'Выполнено'),
    )
    status = models.CharField(
        max_length=16,
        choices=REQUEST_STATUS,
        default='Новая',
        blank=True,
        verbose_name="Статус")

    owner = models.ForeignKey(AdvUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.application_title
