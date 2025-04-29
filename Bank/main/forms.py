from django import forms
from django.contrib.auth.models import User
from .models import Owner

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    Name = forms.CharField()
    Secondname = forms.CharField()
    State = forms.CharField()
    Number = forms.CharField()
    Birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']