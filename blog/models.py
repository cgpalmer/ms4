from django.db import models
from products.models import Product

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    story = models.TextField()
    sku = models.CharField(max_length=254, null=True, blank=True)
    product = models.ForeignKey('products.Product', null=True, blank=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=254, null=True, blank=True)
    date_taken = models.CharField(max_length=254, null=True, blank=True)

    def get_title(self):
        return self.title

   
    
    

        
    