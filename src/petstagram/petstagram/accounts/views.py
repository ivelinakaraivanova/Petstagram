from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.accounts.forms import LogInForm, RegisterForm, ProfileForm
from petstagram.accounts.models import Profile
from petstagram.pets.models import Pet


def login_user(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = LogInForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm()

    user_pets = Pet.objects.filter(user_id=request.user.id)

    context = {
        'form': form,
        'pets': user_pets,
        'profile': profile,
    }

    return render(request, 'accounts/user_profile.html', context)
