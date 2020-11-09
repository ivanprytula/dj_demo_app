from django.shortcuts import render
from django.views.generic import TemplateView

from blog.forms import CommentForm
from blog.models import Post, Comment


class BlogHomeView(TemplateView):
    """View for blog home page."""

    template_name = 'blog/blog_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created_at')
        return context


# class BlogCategory(TemplateView):
#     """It takes a category name as an argument and
#     query the Post database for all posts that have been assigned
#     the given category."""
#
#     template_name = 'blog/blog_category.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = kwargs.get('category')
#         context['posts_with_given_category'] = Post.objects. \
#             filter(categories__name__contains=context['category']). \
#             order_by('-created_at')
#         return context


# def blog_index(request):
#     posts = Post.objects.all().order_by('-created_at')
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/blog_index.html', context)


def post_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category
                                ).order_by('-created_at')

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/blog_category.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    # We create empty form when user visits a page
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                content=form.cleaned_data['content'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)
