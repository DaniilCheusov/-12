from django.urls import path
from . import  views
from django.contrib.auth import views as authViews

from .views import LoginUser


urlpatterns = [
    path('regist', views.regist, name='regist'),
    path('login', LoginUser.as_view(), name='login'),
    path('exit', authViews.LogoutView.as_view(next_page='home'), name='exit'),
    path('Personal_area', views.Personal_area, name='Personal_area'),
    path('Service1', views.Service1, name='Service1'),
    path('Service2', views.Service2, name='Service2'),
    path('Service3', views.Service3, name='Service3'),
    path('Service4', views.Service4, name='Service4'),
    path('Service5', views.Service5, name='Service5'),
    path('Service6', views.Service6, name='Service6'),
    path('Service7', views.Service7, name='Service7'),
]