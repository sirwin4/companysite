from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from . import models
#
#from django.forms.models import inlineformset_factory
from django.forms import ModelForm
from django.db.models import Q
import re
from django.core.validators import validate_email
from .models import Address
from django.forms import ModelChoiceField, ModelMultipleChoiceField


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['city','state','zipcode','street','apartment']
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']