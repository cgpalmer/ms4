from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from basket.views import view_basket, add_to_basket, edit_basket, delete_basket_item, empty_basket

class TestUrls(SimpleTestCase):

    def test_view_basket_url_resolves(self):
        url = reverse('view_basket')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_basket)

    def test_add_to_basket_url_resolves(self):
        url = reverse('add_to_basket', args=['item_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_to_basket)

    def test_edit_basket_url_resolves(self):
        url = reverse('edit_basket')
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_basket)

    def test_delete_basket_item_url_resolves(self):
        url = reverse('delete_basket_item', args=['item_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_basket_item)

    def test_empty_basket_url_resolves(self):
        url = reverse('empty_basket')
        print(resolve(url))
        self.assertEquals(resolve(url).func, empty_basket)
