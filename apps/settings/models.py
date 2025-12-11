from tabnanny import verbose
from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length = 25, verbose_name = "Название сайта")
    logo = models.ImageField(upload_to = "logo/",verbose_name="Логотип сайта")
    icon = models.ImageField(upload_to = "icon/",verbose_name="Иконка сайта")
    descriptions = models.TextField(verbose_name = "Описание")
    phone_number = models.CharField(max_length = 25, verbose_name = "Номер телефона")
    email = models.EmailField(verbose_name = "Электронная почта")
    locate = models.CharField(max_length = 100, verbose_name = "Адрес")

    class Meta:
        verbose_name = "Основная настройка"
        verbose_name_plural = "Основные настройки"