from django.db import models
import random

def Ogenerate_number():
    return str(random.randint(10**8, 10**9 - 1))

def Tgenerate_number():
    return str(random.randint(10**11, 10**12 - 1))


class Owner(models.Model):
    Oaccount = models.CharField(max_length=9, unique=True, default=Ogenerate_number)
    Oname = models.CharField('Name', max_length=15)
    Osecondname = models.CharField('SecondName', max_length=25)
    Ostate = models.CharField('Country', max_length=25)
    Ophone_number = models.CharField('Number', max_length=10)
    Obirth = models.DateField('Birth')

    def __str__(self):
        return f'{self.Oaccount} - {self.Oname} {self.Osecondname}'

class Transactions(models.Model):
    Tvalue = models.DecimalField('Amount', max_digits=12, decimal_places=2)
    Tdate = models.DateTimeField('Date')
    Tnumber = models.CharField(max_length=12, unique=True, default=Tgenerate_number)
    sender = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='sent_transaction')
    receiver = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='received_transaction')

    def __str__(self):
        return f'Transaction: | {self.Tnumber} |'
