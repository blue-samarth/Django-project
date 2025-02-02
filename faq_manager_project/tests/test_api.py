# import pytest
# from django.urls import reverse
# from django.test import TestCase
# from rest_framework.test import APIClient
# from faq_manager.models import FAQ

# class FAQAPITestCase(TestCase):
#     """Test FAQ API translations and list functionality"""
    
#     def setUp(self):
#         self.client = APIClient()
#         self.url = reverse('faq-list')  # Make sure this URL name matches your urls.py
    
#     @pytest.mark.django_db
#     def test_faq_list(self):
#         """Test fetching FAQs API with APIView"""
#         FAQ.objects.create(
#             question="What is DRF?",
#             answer="DRF is Django's API framework."
#         )
        
#         response = self.client.get(self.url)
#         print("Response Status Code:", response.status_code)
#         print("Response Data:", response.data)
        
#         self.assertEqual(response.status_code, 200)
#         self.assertGreater(len(response.data), 0)
#         self.assertEqual(response.data[0]['question'], "What is DRF?")
    
#     @pytest.mark.django_db
#     def test_faq_translation(self):
#         """Test fetching translated FAQ"""
#         faq = FAQ.objects.create(
#             question="Hello",
#             answer="Hi"
#         )
#         faq.question_hi = "नमस्ते"
#         faq.save()
        
#         response = self.client.get(f"{self.url}?lang=hi")
#         print("Response Status Code:", response.status_code)
#         print("Response Data:", response.data)
        
#         self.assertEqual(response.status_code, 200)
#         self.assertIsInstance(response.data, list)
#         self.assertGreater(len(response.data), 0)
#         self.assertEqual(response.data[0]['question'], "नमस्ते")