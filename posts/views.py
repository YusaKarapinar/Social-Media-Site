from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment,PostImage
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseForbidden
from .forms import CommentForm
from django.utils.timezone import now
from datetime import timedelta


@login_required(login_url='/login/')
def feed_page(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            if 'image' in request.FILES:
                post.image = request.FILES['image']
            post.author = request.user
            post.save()
            return redirect('feed_page')

    # Fetch posts from the last 24 hours
    recent_posts = Post.objects.filter(
        created_at__gte=now() - timedelta(days=1)
    ).order_by('-created_at')

    context = {
        'form': PostForm(),
        'recent_posts': recent_posts,
    }
    return render(request, 'posts/feed.html', context)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Beğeniyi kaldır
    else:
        post.likes.add(request.user)  # Beğeniyi ekle
    
    return redirect('feed_page')


@login_required
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Böyle bir gönderi bulunamadı.")

    if post.author != request.user:
        return HttpResponseForbidden("Bu gönderiyi silme izniniz yok.")

    post.delete()
    return redirect("feed_page")

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'posts/post_detail.html', context)