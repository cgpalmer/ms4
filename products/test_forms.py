from django.test import TestCase
from .forms import ProductForm


class TestReviewForm(TestCase):
    def test_product_name_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_product_price_is_required(self):
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_product_special_offer_is_required(self):
        form = ProductForm({'special_offer': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('special_offer', form.errors.keys())
        self.assertEqual(form.errors['special_offer'][0], 'This field is required.')
