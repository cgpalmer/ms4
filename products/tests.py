from django.test import TestCase, SimpleTestCase


class TestViews(TestCase):
    def test_add_product_GET(self):
        response = self.client.get('add_product.html')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/add_product.html')
        

       