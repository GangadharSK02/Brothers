from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    return render(request, 'users/profile_detail.html', {'profile': profile})
