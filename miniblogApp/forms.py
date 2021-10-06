from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from .models import Post
#defineing the ding up form
class SignUpForm(UserCreationForm):#modelFor Inheritance
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="password")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="Confirm Password")
    class Meta:
        model=User
        fields=("username", "first_name","last_name", "email",)
        labels={"email": "Email ID"}
        widgets={"username": forms.TextInput(attrs={"class":"form-control"}),"first_name":forms.TextInput(attrs={"class":"form-control"}),"last_name":forms.TextInput(attrs={"class":"form-control"}),"email":forms.EmailInput(attrs={"class":"form-control"})}
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={"class":"form-control","autocomplete":True}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),strip=False)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title", "desc")
        labels={"desc":"Description"}
        widgets={"title":forms.TextInput(attrs={"class":"form-control"})}
        widgets={"desc":forms.Textarea(attrs={"class":"form-control"})}
