from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'loginform/landing.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = request.POST['role']
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists.')
            return redirect('register')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Create the user or staff account
        try:
            user = User.objects.create_user(username=username,  password=password)
            if role == 'staff':
                user.is_staff = True
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error: {e}")
    
    return render(request, 'loginForm/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('staffdashboard/staff')  # Replace 'staff_dashboard' with the name of your staff dashboard view
            else:
                return redirect('userdashboard/userdash')  # Replace 'user_dashboard' with the name of your user dashboard view
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    
    return render(request, 'loginForm/login.html')
