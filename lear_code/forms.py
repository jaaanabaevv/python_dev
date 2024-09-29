from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from . import models
from django.contrib.auth.models import User

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')
class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = ('title','desc','courses','mentors')
class commentForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'class':'form_control','rows':3,'placeholder':'sizdin komment...'})}
        labels = {'text':''}
