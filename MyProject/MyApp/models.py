from django.db import models

# Create your models here.

class User_Registraion(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    password = models.CharField(max_length=40)
    password1 = models.CharField(max_length=40)
    profile = models.CharField(max_length=40)


class Student_Application(models.Model):
    student_username = models.CharField(max_length=122)
    student_email = models.EmailField(max_length=122)
    Std = models.IntegerField()
    Roll_number = models.IntegerField()
    School_name= models.CharField(max_length=100)
    Address = models.CharField(max_length=60)
    Application_num = models.IntegerField(null=True, blank=True)
    select = [('Pending','Pending'),('Accept','Accept'),('Reject','Reject')]
    status = models.CharField(choices=select,max_length=30,default='Pending')

              