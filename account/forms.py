from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        
class LogForm(forms.Form):
    user_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter Username","class":"form-control bg-transparent text-light"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control bg-transparent text-light"}))