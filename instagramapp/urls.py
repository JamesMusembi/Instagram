from django.urls import path
from instagramapp import views

urlpatterns = [
    path('', views.index, name="index")
]