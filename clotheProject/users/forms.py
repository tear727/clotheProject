from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile
from items.models import Favorite


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user', 'likes', 'dislikes')


class UnfavoriteForm(forms.ModelForm):

    class Meta:
        model = Favorite
        exclude = ('user',)
