from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.staticfiles import finders
from django.http import FileResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import PostForm
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feed/feed.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'feed/feed.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class UserPostListView(ListView):
    model = Post
    template_name = 'feed/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


def fileview(request, pk):
    post = Post.objects.get(pk=pk)
    filename = post.print_file.name.split('/')[-1]
    response = FileResponse(post.print_file.read(),
                            content_type='application/pdf')
    # return response
    return render(request, 'feed/file_view.html', {'file': post.print_file})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('feed-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'feed/about.html', {'title': 'About'})
