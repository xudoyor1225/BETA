from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

def all_applications(request):
    return render(request, 'all_applications.html')

def analytics(request):
    return render(request, 'analytics.html')

def find_scholarships(request):
    return render(request, 'find_scholarships.html')


def help_center(request):
    return render(request, 'help_center.html')

def manage_scholarships(request):
    return render(request, 'manage_scholarships.html')

def my_applications(request):
    return render(request, 'my_applications.html')

def profile_settings(request):
    return render(request, 'profile_settings.html')

def security(request):
    return render(request, 'security.html')

def submit_application(request):
    return render(request, 'submit_application.html')

def users(request):
    return render(request, 'users.html')