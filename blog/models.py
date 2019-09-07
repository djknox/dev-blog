from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    """Model representing a tag for a blog post."""
    name = models.CharField(max_length=200, help_text='Enter a tag for a blog post (e.g. Django, Laravel, Docker, etc.)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this tag."""
        return reverse('tag-detail', args=[str(self.id)])


class Post(models.Model):
    """Model representing a blog post."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # a Post can have many Tags, and a Tag can have many Posts
    tags = models.ManyToManyField(Tag, help_text='Select tags for this post')

    class Meta:
        ordering = ['-published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this post."""
        return reverse('post-detail', args=[str(self.slug)])