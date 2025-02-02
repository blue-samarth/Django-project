from rest_framework.test import APIClient
from django.test import TestCase
from faq_manager.models import FAQ


class FAQAPITestCase(TestCase):
    """Test FAQ API translations and list functionality"""

    def setUp(self):
        """Set up the test environment"""
        self.client = APIClient()

    def test_faq_list(self):
        """Test fetching FAQs API with APIView"""
        FAQ.objects.create(question="What is DRF?", answer="DRF is Django's API framework.")

        response = self.client.get('/api/faqs/')  # Ensure this matches your urlpatterns
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)  # Ensure it's not empty
        self.assertEqual(response.data[0]['question'], "What is DRF?")  # Check that the question is correct

    def test_faq_translation(self):
        """Test fetching translated FAQ"""
        faq = FAQ.objects.create(question="Hello", answer="Hi")
        faq.question_hi = "नमस्ते"
        faq.save()

        response = self.client.get('/api/faqs/?lang=hi')
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)  # Ensure response is a list
        self.assertGreater(len(response.data), 0)  # Ensure it's not empty
        self.assertEqual(response.data[0]['question'], "नमस्ते")  # Check translation
