from blog.views import *
from django.urls import path

urlpatterns = [
    # path("post/<int:pk>",post_detail_view, name='post-detail'),
    path("",PostListView.as_view(), name='blog'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]