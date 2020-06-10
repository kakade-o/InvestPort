from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='investport/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='investport/logout.html'), name='logout'),
    # path('profile', views.profile, name='profile'),
    # path('login/', auth_views.LoginView.as_view(template_name='investport/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='investport/logout.html'), name='logout'),

]