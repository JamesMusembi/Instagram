from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Image, Profile, Comments
from .forms import NewImageForm,NewProfileForm
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all().order_by('post_date')
    profile = Profile.objects.all()
    return render(request, 'index.html', {'images': images}, {'profile': profile})

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
    images = Image.objects.filter(username= current_user)
    # images = Image.objects.all()
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user
            profile.save()
        return redirect('myaccount')

    else:
        form = NewProfileForm()
    return render(request, 'profile.html', {"form": form},  {'images': images}) 

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
       form=NewProfileForm(request.POST,request.FILES)
       Profile.objects.filter(bio = user_edit)
       if form.is_valid():
           form.save()
           return redirect('myaccount')
   else:
          form = NewProfileForm()
   return render(request,'editProfile.html',locals())