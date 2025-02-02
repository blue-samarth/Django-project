import pytest
from faq_manager.models import FAQ


@pytest.mark.django_db
def test_faq_creation():
    # Create FAQ entry
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )

    # Verify creation of English question and answer
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a high-level Python web framework."

@pytest.mark.django_db
def test_translation_on_save():
    """Test that translations are generated when saving a new FAQ"""
    # Create FAQ entry synchronously
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework."
    )
    
    # Verify translations are auto-generated
    assert faq.question_hi is not None
    assert faq.question_bn is not None
    assert len(faq.question_hi) > 0
    assert len(faq.question_bn) > 0

    # Clean up
    # faq.delete()

@pytest.mark.django_db
def test_get_translated_question():
    # Create FAQ entry with translations
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a high-level Python web framework.",
        question_hi="Django क्या है?",
        question_bn="Django কি?",
    )

    # Test getting question in different languages
    assert faq.get_translated_question('hi') == "Django क्या है?"
    assert faq.get_translated_question('bn') == "Django কি?"
    assert faq.get_translated_question('en') == "What is Django?"

