from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='blog_index'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<category>/', views.post_category, name='post_category'),
]
