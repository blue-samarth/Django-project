import pytest
from django.contrib.admin.sites import site
from faq_manager.models import FAQ
from faq_manager.admin import FAQAdmin

@pytest.mark.django_db
def test_faq_admin_registered():
    """Test if FAQ model is registered in Django Admin."""
    assert isinstance(site._registry[FAQ], FAQAdmin)
