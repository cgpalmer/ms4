from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Review(models.Model):
    product = models.ForeignKey('products.Product', null=True, blank=True, on_delete=models.SET_NULL)
    review_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],
                                        null=False, blank=False)
    user = models.CharField(max_length=254, null=False, blank=False, default="User not found")
    review_content = models.TextField(default="")

    def get_friendly_name(self):
        return self.review_rating

    def get_review_content(self):
        return self.review_content
