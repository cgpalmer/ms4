from django.db import models
from products.models import Product

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey('products.Product', null=True, blank=True, on_delete=models.SET_NULL)
    review_rating = models.IntegerField(null=False, blank=False)
    review_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.review_rating

    def get_review_content(self):
        return self.review_content
