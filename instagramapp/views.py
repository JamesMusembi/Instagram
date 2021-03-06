from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
# from .forms import NewImageForm
import datetime as dt

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Q 
from django.views.generic import TemplateView, ListView
from .forms import ProfileForm


# Create your views here.

@login_required(login_url='login')
def index(request):
    image=Image.objects.all()
    users=User.objects.all()
    count=0
    c_users=[]
    for user in users:
        if user in request.user.profile.followers.all() or user in request.user.profile.following.all():
            pass
        else:
            if count <= 10:
                if user == request.user:
                    pass
                else:
                    c_users.append(user)
    return render(request,'index.html',{'images':image,'users':c_users})


@login_required(login_url='login')
def addPost(request): 
    if request.method=='POST':
        image=request.FILES.get('photo')
        caption=request.POST.get('caption')
        img=Image(img_name=image.name,image=image,image_caption=caption,profile=request.user)
        img.save_image()
        return redirect('index')
        
    return render(request,'addimage.html')


@login_required(login_url='login')
def profile(request):
    user=User.objects.all()
    # current_user=request.GET.get('user')
    # logged_in_user=request.user.username
    # user_followers=len(FollowersCount.objects.filter(user=current_user))
    # print("number",user_followers)
    # user_following=len(FollowersCount.objects.filter(follower=current_user))
    # print(user_following)
    return render(request,'profile.html',{'user':user})


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
                    # user.profile.fullname=fullname
                    # user.profile.email_phone=email_phone
                    # user.profile.save()
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
            return redirect('index')
        else:
            messages.error(request,'User with this credentials not found')

    return render(request,'registration/login.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def editProfile(request):
    profiles= Profile.objects.get(user=request.user)

  
    if request.method == 'POST':
       
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            
            prof_form.save()
            return redirect('profile')
            
            
    else:
        # user_form = UpdateUserForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)
             
    context={
        # 'user_form': user_form,
        'prof_form': prof_form,
        'profiles': profiles
          
        }
    return render(request,'editprofile.html',context)

@login_required(login_url='login')
def addComment(request,image_id):
    if request.method=='POST':
        img=Image.objects.get(id=image_id)
        comment=request.POST.get('comment')
        com=Comment.objects.create(user=request.user,img=img,comment=comment)
        com.save()
        print('comment',comment)
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def addremovelike(request,image_id):
    if request.method=='POST':
        img=Image.objects.get(id=image_id)
        if img.likes.contains(request.user):
            img.likes.remove(request.user)
        else:
            img.likes.add(request.user)
    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def addremovefollow(request,user_id):
    if request.method=='POST':
        user=request.user
        new_follow=User.objects.get(id=user_id)
        if user.profile.following.contains(new_follow):
            user.profile.following.remove(new_follow)  
        else:
            user.profile.following.add(new_follow)
        if new_follow.profile.followers.contains(user):
            new_follow.profile.followers.remove(user)
        else:
            new_follow.profile.followers.add(user)
    return redirect(request.META['HTTP_REFERER'])


class SearchResultsView(ListView):
    model = User
    template_name = "search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("query")
        object_list = User.objects.filter(
            Q(username__icontains=query)
        )
        return object_list

