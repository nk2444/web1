from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from blog.models import Post

# Create your views here.
@login_required(login_url='login')
def Homepage(request):
     posts=Post.objects.all()

     return render(request, 'home.html',{'posts':posts}) 

def Signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not same")
        else:
            my_user=User.objects.create_user(username=uname,email=email,password=pass1)
            my_user.save()
        return redirect('login')
    return render(request,'signup.html')

def Loginpage(request):
   if request.method=='POST':
       username=request.POST.get('username')
       pass1=request.POST.get('password')
       print(username,pass1)
       user=auth.authenticate(request,username=username,password=pass1)
       if user is not None:
           auth.login(request,user)
           return redirect('home')
       
       
   return render(request,'login.html')

def Logoutpage(request):
    logout(request)
    return redirect("login")
