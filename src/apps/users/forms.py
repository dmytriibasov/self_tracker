from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import ModelForm
from .models import CardUser
from django import forms


# Forms
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CardUser
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(ModelForm):

    class Meta:
        model = CardUser
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar']


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = CardUser
        fields = ('old_password', 'new_password1', 'new_password2', )

