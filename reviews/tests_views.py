from django.test import TestCase
from .models import Review
from products.models import Product


class TestViews(TestCase):
    def test_add_review_GET(self):
        product = Product.objects.create(name='Review test', price=1.00)
        response = self.client.get(f'/reviews/add/{product.id}/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/add_review.html')

    def test_edit_review_GET(self):
        review = Review.objects.create(review_rating=5, review_content='Good')
        response = self.client.get(f'/reviews/edit/{review.id}/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/edit_reviews.html')
