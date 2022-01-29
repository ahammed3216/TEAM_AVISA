from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=25)
    second_name=models.CharField(max_length=25,null=True,blank=True)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10,null=True,blank=True)
    address=models.TextField()
    panchayath=models.CharField(max_length=20)
    ward=models.IntegerField()
    house_no=models.IntegerField(primary_key=True)
    image=models.ImageField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.first_name



class Jobs(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    jobname=models.CharField(max_length=25)
    employee_name=models.CharField(max_length=25)
    description=models.TextField()
    phonenumber=models.CharField(max_length=10)
    email=models.EmailField()
    location=models.CharField(max_length=25)
    image=models.ImageField()
    created_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    

    def __str__(self):
        return self.employee_name


class Bussiness(models.Model):
    owner_name=models.CharField(max_length=20)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    bussiness_name=models.CharField(max_length=25)
    description=models.TextField()
    type=models.CharField(max_length=30,null=True,blank=True)
    image=models.ImageField()
    location=models.CharField(max_length=25)
    created_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    phonenumber=models.CharField(max_length=10,null=True,blank=True)


    def __str__(self):
        return self.owner_name


class Notification(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    subject=models.CharField(max_length=25)
    text=models.TextField()
    image=models.ImageField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.subject