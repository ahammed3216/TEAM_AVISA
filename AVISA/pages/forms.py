from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model,authenticate


User=get_user_model()

class ProfileForm(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput())
    second_name=forms.CharField(widget=forms.TextInput())
    address=forms.CharField(widget=forms.Textarea())
    email=forms.EmailField()
    phonenumber=forms.CharField()
    panchayath=forms.CharField(widget=forms.TextInput())
    ward=forms.IntegerField()
    house_no=forms.IntegerField(widget=forms.NumberInput)
    image=forms.ImageField()
    



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())



class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    email=forms.EmailField()
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data=self.cleaned_data
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if(password1 != password2):
            raise forms.ValidationError('password want to match eacj other')
        return cleaned_data

    def clean_user_name(self):
        username=self.cleaned_data.get('username')
        username_qs=User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError('Usename exists already !!!')
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('Email already exists !!!')
        return email


class JobForm(forms.Form):
    jobname=forms.CharField()
    employee_name=forms.CharField()
    description=forms.CharField(widget=forms.Textarea)
    phonenumber=forms.CharField()
    email=forms.EmailField()
    location=forms.CharField()
    image=forms.ImageField()

class BussinessForm(forms.Form):
    owner_name=forms.CharField()
    bussiness_name=forms.CharField()
    description=forms.CharField(widget=forms.Textarea)
    sector=forms.CharField()
    image=forms.ImageField()
    location=forms.CharField()
    phonenumber=forms.CharField()

class NotificationForm(forms.Form):
    subject=forms.CharField()
    text=forms.CharField(widget=forms.Textarea)
    image=forms.ImageField()
    