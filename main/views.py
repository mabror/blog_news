from os import name
from django.shortcuts import redirect, render, get_object_or_404
from .forms import LoginForm, RegisterForm, PostForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from apple.decorators import anonymous_required
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post, Comment, PostLIke, Group
from django.core.paginator import Paginator
from django.views.generic import ListView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin


class Index(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-post_added']
    paginate_by = 4
    template_name = 'main/index.html'

    def get_queryset(self):
        query = super().get_queryset()

        title = self.request.GET.get("title")
        if title:
            query = query.filter(title_uz__icontains=title)
        content = self.request.GET.get("content")
        if content:
            query = query.filter(content_uz__icontains=content)

        # print(query.query)
        return query


@permission_required('main.add_comment')
def comment(request, id):
    post = get_object_or_404(Post, id=id)
    posts = Post.objects.get(id=id)
    comment = Comment.objects.filter(post=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return redirect('main-page')
    form = CommentForm()
    context = {
        'form': form,
        'comments': comment,
        'post': post,
        'posts': posts,
    }
    return render(request, 'main/comment.html', context)


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


@permission_required('main.add_post')
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


class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'main/post_edit.html'
    fields = ['title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'photo']

    def test_func(self):
        obj = self.get_object()
        return self.request.user.is_superuser or obj.user == self.request.user


class PostDetail(DetailView):
    model = Post
    template_name = 'main/posts.html'
    context_object_name = 'post'


# @login_required
# def post_edit(request, id):
#     post = Post.objects.get(id=id)
#     # user = User.objects.get(username=post.author)
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('main-page')
#
#     form = PostForm(instance=post)
#     return render(request, 'main/post_edit.html', {'form': form, 'id': id, 'post': post, })


def add_like(request, id):
    if PostLIke.objects.filter(user=request.user, post_id=id).exists():
        return redirect('main-page')

    post = Post.objects.get(id=id)
    post.like += 1
    post.save()

    PostLIke(post=post, user=request.user).save()

    return redirect('main-page')
