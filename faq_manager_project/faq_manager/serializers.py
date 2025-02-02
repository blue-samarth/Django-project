from rest_framework import serializers
from faq_manager.models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    """Serializer for FAQ Model with Language Support"""

    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        feilds = ['id', 'question', 'answer', 'created_at']

    def get_question(self, obj: FAQ) -> str:
        """Return Translated Question Based on Request's lang parameter"""
        lang: str = self.context.get('request').query_params.get('lang', 'en') if self.context.get('request') else 'en'
        return obj.get_translated_question(lang)

    def get_answer(self, obj: FAQ) -> str:
        """Return answer (WYSIWYG rich text)"""
        return obj.answer
