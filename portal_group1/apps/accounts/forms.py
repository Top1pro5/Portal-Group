from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post,Forum

class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'header_image']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image', 'video']
        labels = {
            'content': 'Текст поста',
            'image': 'Выберите изображение',
            'video': 'Выберите видеофайл',
        }
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Что нового?', 'rows': 3}),
        }

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['content','image']
        labels = {
            'content': 'Текст',
            'image': 'Выберите изображение',
        }
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Ваше мнение?', 'rows': 3}),
        }