from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from frontend.models import Player  # Import the Player model

def register(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()
            
            # Create a Player instance for the new user
            Player.objects.create(player=user)

            # Log in the user immediately after registration
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Wordle!')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    """
    Render the user profile page.
    """
    return render(request, 'accounts/profile.html')


def custom_login(request):
    """
    Custom login view to handle login functionality.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful! Welcome back!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def custom_logout(request):
    """
    Log the user out and redirect to the home page.
    """
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')