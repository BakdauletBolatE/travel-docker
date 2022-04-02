from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Country(models.Model):

    name = models.CharField(max_length=255,default='Kazakhstan',verbose_name='Название')
    icon = models.ImageField(upload_to='Country/',null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

class TravelCity(models.Model):

    name = models.CharField(max_length=255,verbose_name='Название')
    description = models.TextField(max_length=255,verbose_name='Описание')
    city_name = models.CharField(max_length=255,verbose_name='Название города')
    image = models.ImageField(upload_to='City/',verbose_name='Фотография города')
    price = models.IntegerField(verbose_name='Цена')
    country = models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name='Страна')

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Городы'




class HotelToCity(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название')
    description = models.TextField(max_length=255,verbose_name='Описание',blank=True,null=True)
    star = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Hotel/')
    city = models.ForeignKey(TravelCity,on_delete=models.CASCADE, related_name='hotels')
    link_to = models.CharField(null=True,blank=True,max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Отел'
        verbose_name_plural = 'Отелы'




class FlightCompany(models.Model):

    name = models.CharField(max_length=255,verbose_name='Название')
    description = models.TextField(max_length=255,verbose_name='Описание',blank=True,null=True)
    image = models.ImageField(upload_to='FlightCompany/')

    def __str__(self) -> str:
        return f"{self.name}"


    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компаний'

class FlightToCity(models.Model):

    company = models.ForeignKey(FlightCompany,on_delete=models.CASCADE)
    wait_time = models.CharField(null=True,blank=True,max_length=255)
    start_time = models.CharField(null=True,blank=True,max_length=255)
    from_to = models.CharField(null=True,blank=True,max_length=255)
    link_to = models.CharField(null=True,blank=True,max_length=255)
    city = models.ForeignKey(TravelCity,on_delete=models.CASCADE, related_name='flights')

    def __str__(self) -> str:
        return f"{self.company.name} - {self.wait_time} - {self.city.name}"


    class Meta:
        verbose_name = 'Авияперелет'
        verbose_name_plural = 'Авияперелеты'


class TravelEvent(models.Model):

    travelCity = models.ForeignKey(TravelCity,on_delete=models.CASCADE,verbose_name='Город')
    start_date = models.DateTimeField(verbose_name='Дата начало')
    end_date = models.DateTimeField(verbose_name='Дата окончание')

    def __str__(self) -> str:
        return f"Тур: {self.travelCity.name}"

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

class Gallery(models.Model):

    name = models.CharField(max_length=255,verbose_name='Названия')
    image = models.ImageField(upload_to='Gallery/',verbose_name='Фотография')

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерей'

class UserEvent(models.Model):
    event = models.ForeignKey(TravelEvent,on_delete=models.CASCADE,verbose_name='Город')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders',verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True,verbose_name='Дата создание')

    def __str__(self) -> str:
        return f"Заказ: {self.event.travelCity.name}"
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
