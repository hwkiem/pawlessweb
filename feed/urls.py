from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    path('full/', PostListView.as_view(), name='feed-full'),
    path('', views.curuser_redirectlist, name='feed-home'),
    path('user/<str:username>/<int:postnum>/',
         UserPostListView.as_view(), name='user-posts'),
    path('user/<str:username>/<int:postnum>/view/',
         views.userpostview, name='user-post-view'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/fileview', views.fileview, name='post-file'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='feed-about'),
]
