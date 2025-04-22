from django import forms
from django.contrib.auth.models import User
from .models import Owner

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    Oname = forms.CharField()
    Osecondname = forms.CharField()
    Ostate = forms.CharField()
    Onumber = forms.CharField()
    Obirth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']