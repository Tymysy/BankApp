from django import forms
from django.contrib.auth.models import User
from .models import Owner, Transactions

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    Name = forms.CharField()
    SecondName = forms.CharField()
    State = forms.CharField()
    Number = forms.CharField()
    Birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['Name', 'SecondName', 'account', 'Number', 'State', 'Birth']
        widgets = {
            'Birth': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account'].widget.attrs['readonly'] = True

class TransactionForm(forms.ModelForm):
    receiver_input = forms.CharField(label='Receiver Account', max_length=9)

    class Meta:
        model = Transactions
        fields = ['Tvalue', 'sender', 'receiver_input']

    def __init__(self, *args, **kwargs):
        sender = kwargs.pop('sender', None)
        super().__init__(*args, **kwargs)

        if sender:
            self.fields['sender'].initial = sender
            self.fields['sender'].disabled = True

    def clean_receiver_input(self):
        account = self.cleaned_data['receiver_input']
        try:
            receiver = Owner.objects.get(account=account)
        except Owner.DoesNotExist:
            raise forms.ValidationError('User not found')
        return receiver

    def save(self, commit=True):
        transaction = super().save(commit=False)
        transaction.receiver = self.cleaned_data['receiver_input']
        if commit:
            transaction.save()
        return transaction