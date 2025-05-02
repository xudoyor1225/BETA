from django.urls import path
from django.contrib.auth.views import LoginView
from appx import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('all/', views.all_applications, name='all_applications' ),
    path('analytics/', views.analytics, name='analytics'),
    path('find/', views.find_scholarships, name='find_scholarships'),
    path('help/', views.help_center, name='help_center'),
    path('manage_scholarships/', views.manage_scholarships, name='manage_scholarships'),
    path('my_applications/', views.my_applications, name='my_applications'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('security/', views.security, name='security'),
    path('submit_application/', views.submit_application, name='submit_application'),
    path('users/', views.users, name='users'),
    ]