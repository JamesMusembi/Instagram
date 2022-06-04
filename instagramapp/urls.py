from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image$', views.new_post, name='new_post'),
    url(r'^new/profile$', views.profile, name='profile'),
    url(r'^myaccount$',views.myaccount,name = 'myaccount'),
    url(r'^new/edit_profile$', views.edit_profile, name='edit_profile'),
    


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  