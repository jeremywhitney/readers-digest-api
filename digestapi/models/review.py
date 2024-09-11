from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_written")
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
