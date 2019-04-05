from django.test import TestCase

from shortener.forms import UrlForm


class MyTests(TestCase):
    def test_form_invalid(self):
        form_data = {'full_url': 'invalid_url.'}
        form = UrlForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_form_valid(self):
        form_data = {'full_url': 'https://www.google.com/'}
        form = UrlForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_redirect_with_url_code(self):
        response = self.client.get('/result/success/hr37GR')
        self.assertEqual(response.context_data['url_code'], 'hr37GR')
