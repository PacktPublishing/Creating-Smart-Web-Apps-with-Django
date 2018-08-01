from django.db import models
from django.conf import settings

# Create your models here.


class Blogpost(models.Model):
    title = models.CharField(max_length=240)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, default=None)

    author = models.CharField(max_length=240, db_index=True)
    body = models.TextField()

    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
