from django.contrib import admin
from .models import User_Registraion,Student_Application

# Register your models here.
@admin.register(User_Registraion)
class UserRegistration(admin.ModelAdmin):
    list_display = ('username','email','password','password1','profile')

@admin.register(Student_Application)
class StudentApllication(admin.ModelAdmin):
    list_display = ('student_username','student_email','Std','Roll_number','School_name','Address','Application_num','status')