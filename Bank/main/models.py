from django.contrib.auth.models import User
from django.db import models
import random

def Ogenerate_number():
    return str(random.randint(10**8, 10**9 - 1))

def Tgenerate_number():
    return str(random.randint(10**11, 10**12 - 1))


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.CharField(max_length=9, unique=True, default=Ogenerate_number)
    Name = models.CharField('Name', max_length=15)
    SecondName = models.CharField('SecondName', max_length=25)
    State = models.CharField('Country', max_length=25)
    Number = models.CharField('Number', max_length=10)
    Birth = models.DateField('Birth')
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.account} - {self.Name} {self.SecondName}'

class Transactions(models.Model):
    Tvalue = models.DecimalField('Amount', max_digits=12, decimal_places=2)
    Tdate = models.DateTimeField('Date')
    Tnumber = models.CharField(max_length=12, unique=True, default=Tgenerate_number)
    sender = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='sent_transaction')
    receiver = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='received_transaction')

    def __str__(self):
        return f'Transaction: | {self.Tnumber} |'
