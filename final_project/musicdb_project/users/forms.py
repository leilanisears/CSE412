from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.contrib.auth import authenticate

#from users.models import UserEntity
#from django.forms import ModelForm
#import string, random
#letters = string.ascii_lowercase

#Create forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'country', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image', 'username', 'first_name', 'last_name']

    def clean_username(self):
        user = self.cleaned_data['username']

        try:
            User.objects.exclude(pk.instance.pk).get(username=user)
        except User.DoesNotExist:
            return user
        raise forms.ValidationError('Username "%s" is already in use.' % user)

class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login.")
