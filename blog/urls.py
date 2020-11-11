from django.urls import path

from .views import (
    BlogListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    BlogCategory,
)

app_name = 'blog'
urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/', PostDetailView, name='post_detail'),
    path('<int:pk>/update', PostUpdateView, name='post_update'),
    path('<int:pk>/delete', PostDeleteView, name='post_delete'),
    path('<category>/', BlogCategory.as_view(), name='post_category'),
]
