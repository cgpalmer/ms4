from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Special(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    special_offer = models.ForeignKey('Special', null=True, blank=True, on_delete=models.SET_NULL)
    ratingreviews = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url_mobile = models.URLField(max_length=1024, null=True, blank=True)
    image_url_desktop = models.URLField(max_length=1024, null=True, blank=True)
    image_mobile = models.ImageField(null=True, blank=True)
    image_desktop = models.ImageField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    sku = models.CharField(max_length=254)
    username = models.CharField(max_length=254)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name
