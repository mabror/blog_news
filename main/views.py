from os import name
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm, PostForm
from django.contrib.auth import authenticate, login, logout
from apple.decorators import anonymous_required
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView


class index(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-post_added']
    paginate_by = 2
    template_name = 'main/index.html'


@anonymous_required('main-page')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main-page')
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'main/auth.html', context)


@anonymous_required('main-page')
def register_post(request):
    form = RegisterForm(request.POST)
    if not form.is_valid():
        return render(request, 'main/auth.html', {'form': form})

    form.save()
    return redirect('main-page')


@anonymous_required('main-page')
def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect('main-page')

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'main/login.html', context)


@login_required
def logout_check(request):
    logout(request)
    return redirect('main-page')


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main-page')

    form = PostForm()
    return render(request, 'main/post_create.html', {'form': form})


@login_required
def post_edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main-page')

    form = PostForm(instance=post)
    return render(request, 'main/post_edit.html', {'form': form, 'id': id, 'post': post})


def posts(request, id):
    post = Post.objects.get(id=id)
    form = PostForm({'title': post.title, 'content': post.content, 'photo': post.photo})
    return render(request, 'main/posts.html', {'id': id, 'post': post, 'form': form})
