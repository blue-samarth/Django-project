import pytest
from django.core.cache import cache


pytest_plugins = [
    "pytest_asyncio",
]

@pytest.fixture(autouse=True)
def clear_cache():
    """It would automatically clear the cache"""
    cache.clear()