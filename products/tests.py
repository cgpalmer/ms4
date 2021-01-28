from django.test import TestCase, SimpleTestCase
from django.test import Client
from django.urls import reverse, resolve
from profiles.views import admin_profile
from .models import Product, Category, Special
from .forms import ProductForm

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

    def test_delete_product(self):
        product = Product.objects.create(name='Delete test', price=1.00)
        response = self.client.get(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/profile/admin/')
        existing_products = Product.objects.filter(id=product.id)
        self.assertEqual(len(existing_products), 0)


class TestModels(TestCase):
    def test_product_rating_is_0(self):
        product = Product.objects.create(name='Delete test', price=1.00)
        self.assertTrue(product.rating == 0)

    def test_product_digital_download_is_false(self):
        product = Product.objects.create(name='Delete test', price=1.00)
        self.assertFalse(product.digital_download)