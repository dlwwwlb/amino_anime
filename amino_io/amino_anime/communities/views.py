from django.shortcuts import render
from .models import Community

def home(request):
    # Покажем последние 6 сообществ на главной
    communities = Community.objects.all().order_by('-created_at')[:6]
    return render(request, 'home.html', {'communities': communities})

def community_list(request):
    communities = Community.objects.all().order_by('-created_at')
    return render(request, 'communities/list.html', {'communities': communities})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommunityForm

@login_required
def community_create(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            community = form.save(commit=False)
            community.creator = request.user
            community.save()
            # Добавляем создателя в участники (через Membership)
            from .models import Membership
            Membership.objects.create(user=request.user, community=community, role='admin')
            messages.success(request, f'Сообщество "{community.name}" создано!')
            return redirect('communities:detail', pk=community.pk)
    else:
        form = CommunityForm()
    return render(request, 'communities/create.html', {'form': form})

def community_detail(request, pk):
    community = get_object_or_404(Community, pk=pk)
    posts = community.posts.all().order_by('-created_at')
    return render(request, 'communities/detail.html', {
        'community': community,
        'posts': posts,
    })

@login_required
def community_join(request, pk):
    community = get_object_or_404(Community, pk=pk)
    if request.user not in community.members.all():
        Membership.objects.create(user=request.user, community=community, role='member')
        messages.success(request, 'Вы вступили в сообщество!')
    else:
        messages.info(request, 'Вы уже участник.')
    return redirect('communities:detail', pk=pk)