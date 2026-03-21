from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm, PostForm, ForumForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Post, Forum
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
# Create your views here.

def home_view(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'home.html', {'posts': posts, 'form': form})

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


@login_required
def profile_view(request, username=None):
    if username is None:
        profile_user = request.user
    else:
        profile_user = get_object_or_404(User, username=username)

    profile, created = Profile.objects.get_or_create(user=profile_user)

    user_posts = Post.objects.filter(author=profile_user).order_by('-created_at')

    form = None
    if profile_user == request.user:
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('profile', username=request.user.username)
        else:
            form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'user_posts': user_posts,
        'form': form,
        'is_owner': profile_user == request.user
    })


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author == request.user:
        post.delete()

    return redirect('home')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    comments = post.replies.all().order_by('created_at')

    form = ForumForm()

    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)

    return render(request, 'post.html', {
        'post': post,
        'comments': comments,
        'form': form
    })