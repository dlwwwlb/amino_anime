from django.shortcuts import render
from .models import Community, Membership

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
from django.contrib.auth.models import User

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
    user_role = community.user_role(request.user) if request.user.is_authenticated else None
    return render(request, 'communities/detail.html', {
        'community': community,
        'posts': posts,
        'user_role': user_role,
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


@login_required
def community_manage(request, pk):
    community = get_object_or_404(Community, pk=pk)
    if not community.is_admin(request.user):
        messages.error(request, 'У вас нет прав администратора.')
        return redirect('communities:detail', pk=pk)

    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES, instance=community)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщество обновлено.')
            return redirect('communities:manage', pk=pk)
    else:
        form = CommunityForm(instance=community)

    members = community.membership_set.all().order_by('user__username')
    return render(request, 'communities/manage.html', {
        'community': community,
        'form': form,
        'members': members,
    })


@login_required
def community_set_role(request, pk, user_id):
    community = get_object_or_404(Community, pk=pk)
    if not community.is_admin(request.user):
        messages.error(request, 'У вас нет прав администратора.')
        return redirect('communities:detail', pk=pk)

    target_user = get_object_or_404(User, pk=user_id)
    membership = get_object_or_404(Membership, community=community, user=target_user)

    if request.method == 'POST':
        role = request.POST.get('role')
        if role in ['member', 'moderator', 'admin']:
            membership.role = role
            membership.save()
            messages.success(request, f'Роль {target_user.username} обновлена.')
        else:
            messages.error(request, 'Некорректная роль.')

    return redirect('communities:manage', pk=pk)