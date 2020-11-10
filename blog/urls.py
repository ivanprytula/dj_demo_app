from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', views.PostDetailView, name='post_detail'),
    path('<int:pk>/update', views.PostUpdateView, name='post_update'),
    path('<int:pk>/delete', views.PostDeleteView, name='post_delete'),
    path('<category>/', views.BlogCategory.as_view(), name='post_category'),
]
