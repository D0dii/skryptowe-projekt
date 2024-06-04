from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tags', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'basic-input', 'placeholder': 'Enter title'}),
            'tags': forms.TextInput(attrs={'class': 'basic-input', 'placeholder': 'Enter tags'}),
            'content': forms.Textarea(attrs={'class': 'basic-input', 'placeholder': 'Enter content'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'w-100'}),
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'password1': None,
            'password2': None,
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.Form):
    query = forms.CharField(label=False, max_length=100, required=False, widget=TextInput(attrs={'placeholder': 'Search for posts...', 'class': 'input search-input'}))


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': None,
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'submit-btn'})
        }