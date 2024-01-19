from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# Create your views here.
# @login_required(login_url='login')
@never_cache
def HomePage(request):
  # if request.user.is_authrnticated():
  if "user" in request.session:
    username=request.session['user']

    context1={
      "name":username
    }

    return render(request,'home.html',context1)
  
  else:
    return redirect('login')


@never_cache
def SignupPage(request):
  if 'user' in request.session:
    return redirect('home')
  
  if request.method=="POST":
    uname=request.POST.get('username')
    email=request.POST.get('email')
    pass1=request.POST.get('password1')
    pass2=request.POST.get('password2')


    if not (uname and email and pass1 and pass2):
      return render(request,'signup.html',{'error_message': 'Please fill Required fields! '})

    elif User.objects.filter(username=uname).exists():
      return render(request,'signup.html',{'error_user':'Username already exists'})
    
    elif User.objects.filter(email=email).exists():
      return render(request,'signup.html',{'error_email':'Email already exists'})
    
    elif pass1!=pass2:
      return render(request,'signup.html',{'error_pass': 'Password mismatch '})
      
    else:
       user=User.objects.create_user(username=uname,email=email,password=pass1)
       user.save()
       return redirect('login')
      
    

  
  return render(request,"signup.html")


@never_cache
def loginPage(request):
  if 'user' in request.session:
    return redirect('home')
  
  else:

   if request.method=="POST":
    username=request.POST.get("username")
    pass1=request.POST.get("pass")

    user=authenticate(request,username=username,password=pass1)
    if user is not None:
      # login(request,user)
      request.session['user']=username
      return redirect('home')
    
    else:
      return render(request,"login.html",{'error_message':'Invalid username or password'})

  
  return render(request,'login.html')



def LogoutPage(request):
  if 'user' in request.session:
    request.session.flush()
    # logout(request)
  return redirect('login')

