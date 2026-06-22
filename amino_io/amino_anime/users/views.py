from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'profile_user': user})