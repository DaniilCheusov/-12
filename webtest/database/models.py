import database.models
from django.db import models


class Halls(models.Model):
    Hall_ID = models.BigAutoField('ID', primary_key=True)
    Hall_Name = models.CharField('Назавние зала', max_length=10, null=True, blank=True, default=" ", unique=True)
    Price_Weekdays_8_17 = models.PositiveSmallIntegerField('Стоимость 1 часа с 8 до 17')
    Price_Weekdays_17_8 = models.PositiveSmallIntegerField('Стоимость 1 часа с 17 до 8')
    Price_Weekends_8_17 = models.PositiveSmallIntegerField('Стоимость 1 часа с 8 до 17')
    Price_Weekends_17_8 = models.PositiveSmallIntegerField('Стоимость 1 часа с 17 до 8')

    def __str__(self):
        return  self.Hall_Name

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'

class Client(models.Model):
    Client_ID = models.BigAutoField('ID', primary_key=True)
    Surname = models.CharField('Фамилия', max_length=20)
    Name = models.CharField('Имя', max_length=20)
    Mid_Name = models.CharField('Отчество', max_length=20)
    Number = models.CharField('номер телефона', max_length=10)
    Email = models.EmailField('Email')
    Date = models.DateTimeField('Дата и время бронирования', null=True)
    Time_range = models.CharField('Время аренды в часах', max_length=2, null=True)
    Type_of_Service = models.ForeignKey('Halls', on_delete=models.PROTECT, null=True, default=1)
    Status = models.BooleanField('Status' ,null=True)

    def __str__(self):
        return  'Новая заявка от ' + self.Surname

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'