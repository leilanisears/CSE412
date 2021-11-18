from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import UserEntity

import string, random
letters = string.ascii_lowercase

#Create forms

class NewUserForm(UserCreationForm):
    user_id = ''.join(random.choice(letters) for i in range(20))
    country = forms.CharField(max_length=100, help_text='Country')
    display_name = forms.CharField(max_length=100, help_text='Display Name')

    class Meta:
        model = UserEntity
        fields = ["USERNAME_FIELD", "display_name", "password1", "password2", "country"]



