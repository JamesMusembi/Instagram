from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import NewImageForm
import datetime as dt

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Q 
from django.views.generic import TemplateView, ListView



# Create your views here.

def welcome(request):
    images=Image.objects.all()
    return render(request, 'index.html',{'images':images})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_user(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"profiles": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
    
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.username = current_user
            image.save()
        return redirect('welcome')

    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})   
 

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id=current_user.id)
    # images = Image.objects.filter(username= current_user)
    # images = Image.objects.all()
    if request.method == 'POST':
        # # form = NewProfileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     profile = form.save(commit=False)
            # profile.username = current_user
            # profile.save()
        # return redirect('myaccount')

    # else:
        # form = NewProfileForm()
     return render(request, 'profile.html',  ) 

@login_required(login_url='/accounts/login/')
def myaccount(request):
  current_user = request.user
  myProfile = Profile.objects.filter(username = current_user).first()
  return render(request, 'timeline.html', {"myProfile":myProfile})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
   current_user=request.user
   user_edit =Profile.objects.filter(username=current_user).first()
   
   if request.method =='POST':
    #    form=NewProfileForm(request.POST,request.FILES)
       Profile.objects.filter(bio = user_edit)
    #    if form.is_valid():
    #        form.save()
        #    return redirect('myaccount')
#    else:
        #   form = NewProfileForm()
   return render(request,'editProfile.html',locals())

@unauthenticated_user
def register(request):
    if request.method=='POST':
        email_phone=request.POST.get('email-phone')
        fullname=request.POST.get('fullname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if password==password1:
            user,create=User.objects.get_or_create(username=username)
            if create:
                try:
                    validate_password(password)
                    user.set_password(password)
                    
                    user.save()
                    messages.success(request,'Account created succesfully')
                    return redirect('login')
                except ValidationError as e:
                    messages.error(request,'Password error {e} ')
                    
            else:
                messages.info(request,'user with these details already exists')
        else:
            messages.error(request,'Passwords do not match')
    return render(request,'registration/registration_form.html')


@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        print('user',user)
        if user is not None:
            login(request,user)
            return redirect('welcome')
        else:
            messages.error(request,'User with this credentials not found')

    return render(request,'registration/login.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')