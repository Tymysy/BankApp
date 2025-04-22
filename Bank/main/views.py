from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .models import Transactions
from .models import Owner
from .forms import UserRegisterForm

def index(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Owner.objects.create(
                user=user,
                Oname=form.cleaned_data['Oname'],
                Osecondname=form.cleaned_data['Osecondname'],
                Ostate=form.cleaned_data['Ostate'],
                Onumber=form.cleaned_data['Onumber'],
                Obirth=form.cleaned_data['Obirth'],
            )

            login(request, user)
            return redirect('owner_profile')
    else:
        form = UserRegisterForm()

    return render(request, 'main/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def my_profile(request):
    owner = request.user.owner
    return render(request, 'main/profile.html', {'owner': owner})