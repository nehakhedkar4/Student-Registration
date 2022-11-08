from django.shortcuts import redirect, render
from .forms import SignUp,ApplicationForm
from .models import User_Registraion,Student_Application
from django.contrib import messages
import random
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# STUDENT-REGISTRATION

# HOME PAGE
def home_page(request):
    return render(request,'home.html')

# USER LOGIN
def user_login(request):
    if request.method == 'POST':
        print("LOGINNNNNNNNNNNNNNNNNNNNNN")
        nm = request.POST['username']
        pw = request.POST['password']   
        
        if User_Registraion.objects.filter(username=nm).exists():
            x = User_Registraion.objects.get(username=nm)
            p = x.password
            check = x.profile
        
            if p==pw:
                request.session['user'] = nm
                if check == 'Faculty':
                    return redirect('/f_dashboard/')
                else:
                    # return HttpResponseRedirect(reverse('s_dashboard',args=[x.id]))
                    return redirect('/ApplicationForm/')
            else:
                print('Incorrect Password ')
                messages.warning(request,'Please Enter correct Password!')
        else:
            print("wwwwwwwwwwwww")
            messages.warning(request,'Please enter correct Username!')

    return render(request,'login.html')

# SIGN UP PAGE
def sign_up(request):    
    if request.method == 'POST':
        # print("Form SUBMITTTTTTTTTTTTTTTTTT")
        fm = SignUp(request.POST)
        # print(fm)
        if fm.is_valid():
            # print("formmmmmmmm validddd")
            name = fm.cleaned_data['username']
            email = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            pw1 = fm.cleaned_data['password1']
            pr = fm.cleaned_data['profile']
            if pw != pw1:
                messages.info(request,'Password does not match!')
                return redirect('/signup/')
            else:
                if User_Registraion.objects.filter(username=name,password=pw).exists():
                    messages.info(request,'User Already exists!!')
                    return redirect('/signup/')
                elif User_Registraion.objects.filter(email=email).exists():
                    messages.info(request,'Email already taken!!')
                    return redirect('/signup/')
                else:
                    reg = User_Registraion.objects.create(username=name,email=email,password=pw,password1=pw1,profile=pr)
                    reg.save()
        return redirect('/login/')
    else:
        fm = SignUp()
    return render(request,'signup.html',{'form':fm})


# STUDENT APPLICATION FORM
def ApplictionForm(request):
    if request.method == 'POST':
        print("APPLICATION FORM FILLED BY STUDENTTT")
        s_form = ApplicationForm(request.POST)
        if s_form.is_valid():
            
            name = s_form.cleaned_data['student_username']
            email = s_form.cleaned_data['student_email']
            Std = s_form.cleaned_data['Std']
            roll_nu = s_form.cleaned_data['Roll_number']
            school_n = s_form.cleaned_data['School_name']
            Address = s_form.cleaned_data['Address']
            
            if Std <=0 and roll_nu <= 0:
                messages.info(request,'Please select correct Std & Roll Number')
                return redirect('/studentForm/')
            elif Std <=0:
                messages.info(request,'Please select correct Std')
                return redirect('/studentForm/')
            elif roll_nu <= 0:
                messages.info(request,'Please select correct Roll Number')
                return redirect('/studentForm/')
            a = Student_Application.objects.create(student_username=name,student_email=email,Std=Std,Roll_number=roll_nu,School_name=school_n,Address=Address)
            a.save()
            g = Student_Application.objects.get(student_username=name)
            print(g.id) 

            return HttpResponseRedirect(reverse('s_dashboard',args=[g.id]))

    return render(request,'ApplicationForm.html',{'a_form' : ApplicationForm()})


# STUDENT DASHBOARD
def s_dashboard(request,id):
    data = Student_Application.objects.get(pk=id)
    print(data)
    # CREATE AN UNIQUE APPLICATION NUMBER FOR EACH STUDENT
    i = True
    n = len(Student_Application.objects.all())
    print("Number of users -------------", n)
    if n != 0:
        print("n IS NOT EQUAL TO ZEROOO-------")
        while i:
            ran_num = random.randrange(111111,999999)
            if Student_Application.objects.filter(Application_num=ran_num):
                i = True
                print("RANDOM NUMBER ALREADY EXITTTTTTTT")
            else:
                i = False
                break
    else:
        ran_num = random.randrange(111111,999999)
    print("RANDOM NUMBER----------------: ",ran_num)

    data.Application_num = ran_num
    data.save()
    print('RANDOM NUM WITH SUBMITTED DATA SAVED----------------------------')
    print(data.status)
    if data.status == 'Pending':
        print("pending--------")
        messages.info(request,f"Your Application Number is '{ran_num}'. It will approve When faculty will accept your Application Request!")
    elif data.status == 'Accepted':
        print("Accepted---------------------")
        messages.success(request,"Your Application Request has been Accepted!")
    elif data.status == 'Rejected':
        messages.warning(request,"Your Application Request has been Rejected!")

    return render(request,'Student_dashboard.html',{'stu':data})


# FACULTY DASHBOARD
def f_dashboard(request):
    data = Student_Application.objects.all()
    return render(request,'Faculty_dashboard.html',{'data':data})

# ACTION BY FACULTY 
def action_data(request,id):
    data = Student_Application.objects.get(pk=id)
    if request.method == 'POST':
        action = request.POST['action']
        data.status = action
        data.save()
        print("STATUS UPDATED-------------------")
        return redirect('/f_dashboard/')
    return render(request,'ActionByfaculty.html',{'id':data})












    # rough

def ren(request):
    if request.method == "POST":
        print("============")
        return render(request,'rdct.html')
    return render(request,'rend.html')

def red(request):
    return redirect('rdct.html')