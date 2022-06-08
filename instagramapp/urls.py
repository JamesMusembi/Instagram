from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('search/', views.search_results, name='search_results'),
    # path('new/image/', views.new_post, name='new_post'),
    path('new/profile/', views.profile, name='profile'),
    path('myaccount/',views.myaccount,name = 'myaccount'),
    path('new/edit_profile/', views.edit_profile, name='edit_profile'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  