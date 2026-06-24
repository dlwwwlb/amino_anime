from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'users/profile.html', {'profile_user': user, 'profile': profile})


@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/edit_profile.html', {'form': form})