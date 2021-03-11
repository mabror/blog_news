from django import forms
import django
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _


class RegisterForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'photo']
        labels = {
            'title': _('Mavzu'),
            'content': _('Kontent'),
            'photo': _('Rasm')
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)