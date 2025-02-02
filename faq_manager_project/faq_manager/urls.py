# faq_manager/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from faq_manager.views import FAQListView

router = DefaultRouter()

urlpatterns = [
    path("faqs/", FAQListView.as_view(), name="faq-list"),
]
