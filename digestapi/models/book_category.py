from django.db import models


class BookCategory(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
