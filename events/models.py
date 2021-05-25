from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import NullBooleanField
import uuid

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default=uuid.uuid1)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
