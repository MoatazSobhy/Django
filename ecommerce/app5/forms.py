from django import forms
from .models import *
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=50, required=True)
#     password = forms.CharField(max_length=50, required=True)
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        