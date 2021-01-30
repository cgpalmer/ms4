from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    # this needs to be unique
    sku = models.CharField(max_length=254, null=False, blank=True)
    name = models.CharField(max_length=254, null=False, blank=False, default="new_product")
    friendly_name = models.CharField(max_length=254, null=False, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True)
    rating = models.IntegerField(default=0)
    number_of_ratings = models.IntegerField(null=True, blank=True, default=0)
    rating_total = models.IntegerField(null=True, blank=True, default=0)
    special_offer = models.ForeignKey('Special', null=True, blank=False, on_delete=models.SET_NULL)
    image_url_mobile = models.URLField(max_length=1024, null=False, blank=True)
    image_url_desktop = models.URLField(max_length=1024, null=False, blank=True)
    image_mobile = models.ImageField(null=False, blank=True)
    image_desktop = models.ImageField(max_length=1024, null=False, blank=True)
    digital_download = models.BooleanField(default=False, null=True, blank=True)
    product_type = models.CharField(max_length=254, null=False, blank=True)
    number_of_pictures = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Special(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True, default="none")
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    discounts = models.DecimalField(max_digits=4, decimal_places=3, default=0.0, null=True, blank=False)

    def __str__(self):
        return self.name
