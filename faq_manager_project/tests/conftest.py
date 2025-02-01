import pytest
from django.core.cache import cache

@pytest.fixture(autouse=True)
def clear_cache():
    """It would automatically clear the cache"""
    cache.clear()