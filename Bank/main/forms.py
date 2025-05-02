from django import forms
from django.contrib.auth.models import User
from .models import Owner

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