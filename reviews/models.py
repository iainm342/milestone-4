from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """
    Review model to allow user to leave a product review
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(default=1)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
