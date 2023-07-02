from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'bio', 'location', 'birth_date']

class EditProfileForm(forms.ModelForm):
  
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'bio', 'location', 'birth_date']
