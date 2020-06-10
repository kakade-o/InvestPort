from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

from . import models, forms


# Create your views here.


def home(request):
    return render(request, 'investport/home.html')

# def signup(request):
#     if request.method == 'POST':
#         form = forms.SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = forms.SignUpForm()
#     return render(request, 'signup.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = forms.SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('')
#     else:
#         form = forms.SignUpForm()
#     return render(request, 'investport/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) # POST => form with the users input
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save() # saves to database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = forms.SignUpForm()
    return render(request, 'investport/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'investport/profile.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'investport/profile.html', context)
