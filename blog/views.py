from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, SearchForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
from django.db.models import Q

def index(request):
    results = Post.objects.all().order_by('-created_at')
    form = SearchForm()
    query = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(
                Q(title__icontains=query) |
                Q(author__username__icontains=query) |
                Q(tags__icontains=query)
            )
    return render(request, 'index.html', {'form': form, 'query': query, 'results': results})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comment_form': comment_form})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')

@login_required
def add_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=pk)


# signup page
def user_signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def follow_unfollow_user(request, username):
    target_user = get_object_or_404(User, username=username)
    if target_user != request.user:
        if target_user.profile in request.user.profile.follows.all():
            request.user.profile.follows.remove(target_user.profile)
        else:
            request.user.profile.follows.add(target_user.profile)
    return redirect('profile', username=target_user.username)

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
        'followers': user.profile.followed_by.all(),
        'follows': user.profile.follows.all(),
    }
    return render(request, 'profile.html', context)

@login_required
def comment_edit(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_edit.html', {'form': form})

@login_required
def following_posts(request):
    form = SearchForm()
    query = None
    user_profile = get_object_or_404(Profile, user=request.user)
    following_profiles = user_profile.follows.all()
    following_users = [profile.user for profile in following_profiles]
    results = Post.objects.filter(author__in=following_users)

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = results.filter(
                Q(title__icontains=query) |
                Q(author__username__icontains=query) |
                Q(tags__icontains=query)
            )

    return render(request, 'following_posts.html', {'form': form, 'query': query, 'results': results})