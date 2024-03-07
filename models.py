from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.
# class CustomUser(AbstractUser):
#     email=models.EmailField(max_length=254,unique=True)
#     username=models.CharField(max_length=50)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS =[]
   
class Employee(models.Model):
    # id=models.AutoField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
class MaterialIn(models.Model):
    part_name = models.CharField(max_length=100)
    date_of_receiving = models.DateField()
    quantity = models.IntegerField()
    w_o_n_o = models.IntegerField()
    challan = models.ImageField(upload_to="challan",default="industrylogo.jpg")

class MaterialOut(models.Model):
    part_name = models.CharField(max_length=100)
    date_of_receiving = models.DateField()
    quantity = models.IntegerField()
    w_o_n_o = models.IntegerField()
    challan = models.ImageField(upload_to="challanout",default="industrylogo.jpg")
  