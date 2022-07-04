from django import forms
from .models import User, Manga
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

class UploadMangaForm(ModelForm):
    class Meta:
        model = Manga
        fields = ['author', 'manga_title', 'manga_cover', 'summary']
