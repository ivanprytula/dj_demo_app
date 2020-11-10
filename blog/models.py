from django.db import models


class Post(models.Model):
    """Post model with MTM relation with Category."""
    title = models.CharField(max_length=255, blank=False, default='Enter title...')
    content = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(to='Category', related_name='posts')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment to post from other user."""
    author = models.CharField(max_length=60)
    content = models.TextField(blank=False, default='Enter your comment...')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Category(models.Model):
    """Categories to which post can belong."""
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
