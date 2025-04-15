from django.shortcuts import render, get_object_or_404
from .models import Transactions
from .models import Owner

def index(request):
    return render(request, 'main/index.html')

def owner_detail(request, oaccount):
    owner = get_object_or_404(Owner, Oaccount=oaccount)
    return render(request, 'main/profile.html', {'owner': owner})