from django.test import TestCase
from .models import Review
from products.models import Product
from .forms import ReviewForm


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


class TestReviewForm(TestCase):
    def test_review_rating_is_required(self):
        form = ReviewForm({'review_rating': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review_rating', form.errors.keys())
        self.assertEqual(form.errors['review_rating'][0], 'This field is required.')

    def test_review_content_is_required(self):
        form = ReviewForm({'review_content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review_content', form.errors.keys())
        self.assertEqual(form.errors['review_content'][0], 'This field is required.')

    def test_review_fields_are_accurate(self):
        form = ReviewForm()
        self.assertNotEquals(form.Meta.exclude, ['user', 'product'])

    def test_review_rating_is_maxed_at_5(self):
        form = ReviewForm({'review_rating': 6})
        self.assertFalse(form.is_valid())
        self.assertIn('review_rating', form.errors.keys())
        self.assertEqual(form.errors['review_rating'][0], 'Ensure this value is less than or equal to 5.')

    def test_review_rating_not_below_0(self):
        form = ReviewForm({'review_rating': -1})
        self.assertFalse(form.is_valid())
        self.assertIn('review_rating', form.errors.keys())
        self.assertEqual(form.errors['review_rating'][0], 'Ensure this value is greater than or equal to 0.')
