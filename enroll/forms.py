from django import forms
from django.db import models
from django.forms import fields, widgets
from django.shortcuts import render
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}), #this form-controll class is a bootstrap class.
            'email': forms.EmailInput(attrs={'class':'form-control'}),
                                    #render_value is using so that we can see our password in the update page.
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'})
        }