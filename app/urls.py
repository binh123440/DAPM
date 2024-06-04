from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/base/', views.base, name="base"),
    path('/charts/', views.charts, name="charts"),
    path('/status/', views.status, name="status"),
    path('/signin/', views.signin, name="signin"),
    path('/signup/', views.signup, name="signup"),
    path('/logout/', views.logout, name="logout"),
    path('/view_detail/<str:mahs>/', views.view_detail, name='view_detail'),
    path('/update_hs/<str:mahs>/', views.update_hs, name='update_hs'),
]
