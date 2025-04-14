from django.db import models

class Owner(models.Model):
    Oname = models.CharField('Name', max_length=15)
    Osecondname = models.CharField('SecondName', max_length=25)
    Ostate = models.CharField('Country', max_length=25)
    Onumber = models.CharField('Number', max_length=10)
    Obirth = models.DateField('Birth')

