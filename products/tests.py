from django.test import TestCase, SimpleTestCase
from django.test import Client
from django.urls import reverse, resolve
from profiles.views import admin_profile
from .models import Product, Category, Special

class TestViews(TestCase):

    def test_add_product_GET(self):
        response = self.client.get('/products/add/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')
    
    def test_add_product_POST(self):
        response = self.client.get('/products/add/', {'name': 'test product'})
        self.assertEquals(response.status_code, 200)
        url = reverse('admin_profile_page')
        self.assertEquals(resolve(url).func, admin_profile)
    
    def test_edit_product_GET(self):
        product = Product.objects.create(name='Edit test', price=1.00)
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
    
    def test_edit_product_POST(self):
        product = Product.objects.create(name='Edit test', price=1.00)
        response = self.client.post(f'/products/edit/{product.id}/')
        self.assertEquals(response.status_code, 200)
        url = reverse('admin_profile_page')
        self.assertEquals(resolve(url).func, admin_profile)
