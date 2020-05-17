from django.db.models.signals import post_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Post

@receiver(post_delete, sender=Post)
def delete_file(sender, instance, *args, **kwargs):
    instance.print_file.delete(save=False)