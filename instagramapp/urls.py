from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns=[
    path('',views.index,name = 'index'),
    path('addpost/',views.addPost,name='addpost'),
    path('profile/',views.profile,name='profile'),
    path('edit/',views.editProfile,name='edit'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('addcomment/<str:image_id>/',views.addComment,name='addcomment'),
    path('addremovelike/<str:image_id>/',views.addremovelike,name='addremovelike'),
    path('addremovefollow/<str:user_id>/',views.addremovefollow,name='addremovefollow'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  