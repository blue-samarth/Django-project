import pytest
from django.core.cache import cache

@pytest.mark.django_db
def test_redis_cache():
    """Test storing and retrieving data from Redis cache"""

    # Step 1: Set a value in the cache
    cache.set("test_key", "Hello Redis!", timeout=30)

    # Step 2: Retrieve the value from the cache
    cached_value = cache.get("test_key")

    # Step 3: Ensure the value is stored correctly
    assert cached_value == "Hello Redis!", "Redis cache is not working correctly"

    # Step 4: Delete the key
    cache.delete("test_key")

    # Step 5: Ensure the key is deleted
    assert cache.get("test_key") is None, "Redis cache key was not deleted"
