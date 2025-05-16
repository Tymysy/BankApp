from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .models import Owner, Transactions
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.decorators import login_required
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



@login_required
def my_profile(request):
    owner = request.user.owner
    profile_form = ProfileForm(request.POST or None, instance=owner)
    transaction_form = TransactionForm(request.POST or None, sender=owner)

    transactions_list = Transactions.objects.filter(
        Q(sender=owner) | Q(receiver=owner)
    ).order_by('-Tdate')

    paginator = Paginator(transactions_list, 10)
    page_number = request.GET.get("page")
    transactions = paginator.get_page(page_number)

    if request.method == 'POST':
        if 'save_profile' in request.POST and profile_form.is_valid():
            profile_form.save()
            return redirect('owner_profile')

        if 'create_transaction' in request.POST and transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            transaction.sender = owner
            transaction.Tdate = timezone.now()

            if transaction.receiver == owner:
                messages.error(request, "You cannot send money to yourself.")
                return redirect('owner_profile')

            if transaction.Tvalue <= 0:
                messages.error(request, "Amount must be positive.")
                return redirect('owner_profile')

            owner = Owner.objects.get(pk=owner.pk)
            receiver = Owner.objects.get(pk=transaction.receiver.pk)

            if owner.balance < transaction.Tvalue:
                messages.error(request, "Not enough balance.")
                return redirect('owner_profile')

            owner.balance -= transaction.Tvalue
            receiver.balance += transaction.Tvalue

            owner.save()
            receiver.save()

            transaction.save()

            messages.success(request, "Transaction completed successfully.")
            return redirect('owner_profile')

    return render(request, 'main/profile.html', {
        'form': profile_form,
        'transaction_form': transaction_form,
        'transactions': transactions,
        'balance': owner.balance,
    })