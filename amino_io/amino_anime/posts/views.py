from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from communities.models import Community
from .models import Post
from .forms import PostForm

@login_required
def post_create(request):
    community_id = request.GET.get('community')
    if not community_id:
        messages.error(request, 'Не указано сообщество.')
        return redirect('communities:list')
    community = get_object_or_404(Community, pk=community_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.community = community
            post.author = request.user
            post.save()
            messages.success(request, 'Пост создан!')
            return redirect('posts:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form, 'community': community})

from comments.models import Comment
from comments.forms import CommentForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent__isnull=True)  # только корневые комментарии
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'posts/detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })