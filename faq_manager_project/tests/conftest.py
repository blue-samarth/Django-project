import pytest
from django.core.cache import cache
from django.conf import settings


pytest_plugins = [
    "pytest_asyncio",
]

@pytest.fixture(autouse=True)
def clear_cache():
    """It would automatically clear the cache"""
    cache.clear()


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite for tests
        'NAME': ':memory:',
    }

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass