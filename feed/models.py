from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.username, filename)


class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    print_file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
