from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .models import Owner, Transactions
from django.utils import timezone
from .forms import UserRegisterForm, ProfileForm, TransactionForm

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
                Name=form.cleaned_data['Name'],
                SecondName=form.cleaned_data['SecondName'],
                State=form.cleaned_data['State'],
                Number=form.cleaned_data['Number'],
                Birth=form.cleaned_data['Birth'],
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
    profile_form = ProfileForm(request.POST or None, instance=owner)
    transaction_form = TransactionForm(request.POST or None, sender=owner)

    if request.method == 'POST':
        if 'save_profile' in request.POST and profile_form.is_valid():
            profile_form.save()
            return redirect('owner_profile')

        if 'create_transaction' in request.POST and transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            transaction.sender = owner
            transaction.Tdate = timezone.now()
            transaction.save()
            return redirect('owner_profile')

    return render(request, 'main/profile.html', {
        'form': profile_form,
        'transaction_form': transaction_form
    })