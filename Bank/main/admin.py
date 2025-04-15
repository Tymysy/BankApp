from django.contrib import admin

# Register your models here.
from .models import Owner
from .models import Transactions

admin.site.register(Owner)
admin.site.register(Transactions)