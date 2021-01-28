from django.test import TestCase

from .forms import ReviewForm

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

    def test_review_fiels_are_accurate(self):
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