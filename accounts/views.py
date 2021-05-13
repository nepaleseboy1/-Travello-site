from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
import random

# Create your views here.
code = random.randint(100000,999999)
def register(request):
    if request.method =='POST':
        global first_name
        global last_name
        global username
        global password1
        global email
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken ")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken ")
                return redirect('register')
            else:
                
                
                
                send_mail(
                    'Verify Your Account',
                    'Hey!'+first_name +' '+ 'your 6 digit verification code is ' +' '+ str(code),
                    'nepaleseboy80@gmail.com',
                    [email],
                    fail_silently= False
                    
                    

                 )
                
                
                return render (request,'verify_email.html')
        else :
            messages.info(request, "Password do not matched ")
            return redirect('register')

    else:
        return render(request,'register.html')
    
    return redirect('/')

def verify_email(request):
        code1= int (request.POST['code1'])
        if code1 == code :
            
            
            user = User.objects.create_user(username=username, password= password1, email = email, first_name = first_name , last_name = last_name)
            user.save()
            
            return redirect('/')
        else:
            messages.info(request,"verification code not matched .")
            return redirect('register')

def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"username or password not correct")
            return redirect('login')
    else:
        return render(request, 'login.html')
        user.is_authenticated==False

def logout(request):
    
    auth.logout(request)
    return redirect('/')

    