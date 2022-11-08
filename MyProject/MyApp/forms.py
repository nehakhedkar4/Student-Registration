from django import forms
from django.forms import ModelForm
from .models import User_Registraion,Student_Application

class SignUp(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(label='Confirm password',widget=forms.PasswordInput())
    ch = (
        ('Student','Student'),
        ("Faculty",'Faculty'),
    )
    profile = forms.ChoiceField(choices=ch)
    
    class Meta():
        model = User_Registraion
        fields = '__all__'
  

    def __init__(self,*args,**kwargs):
        super(SignUp, self).__init__(*args,**kwargs)
        # 
        for fname,f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'


class ApplicationForm(ModelForm):
    class Meta:
        model = Student_Application
        # fields = '__all__'
        fields = ('student_username','student_email','Std','Roll_number','School_name','Address')
        labels = {'student_username':'Your Full name','student_email':'Email Address','Std':'Standard'}
        
        widgets = {
            'student_username': forms.TextInput(attrs={'class':'form-control','placeholder':'Your name'}),
            'student_email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email Address'}),
            'Std':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Standard'}),
            'Roll_number':forms.NumberInput(attrs={'class':'form-control','placeholder': 'Your Roll Number'}) ,
            'School_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Your School name'}) ,
            'Address':forms.TextInput(attrs={'class':'form-control','placeholder': 'Your Address'}) ,

        } 
        

    #   Heroku