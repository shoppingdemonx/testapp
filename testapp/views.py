from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .models import Profile


# Create your views here.
def home(request):
    return render(request,'testapp/dashboard.html')


def signin(request): # login 
    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request,username=username,password=password)
        
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
        
    return render(request,"testapp/login.html")

def signup(request): #register
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        is_teacher = request.POST.get('is_teacher') == 'on'
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exist!!")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exits!!")
            return redirect('signup')
        
        
        user = User.objects.create_user(username=username,email=email,password=password)
        
        
        Profile.objects.create(user=user,is_teacher=is_teacher)
        messages.success(request, "Account created! Please login.")
        return redirect('login')
        
    return render(request,"testapp/signup.html")