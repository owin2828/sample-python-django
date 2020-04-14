from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductsTests(TestCase):

    def setUp(self):
        Product.objects.create(name='AAA', price="20000", stock="3", image_url="www.xx.com")

    def test_text_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.name}'
        self.assertEquals(expected_object_name, 'AAA')

    def test_post_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'AAA')
        self.assertTemplateUsed(response, 'index.html')
