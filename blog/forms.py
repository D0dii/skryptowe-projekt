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

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.Form):
    query = forms.CharField(label=False, max_length=100, required=False, widget=TextInput(attrs={'placeholder': 'Search for posts...', 'class': 'input search-input'}))


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }