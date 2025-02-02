from rest_framework.response import Response
from django.core.cache import cache
from rest_framework.views import APIView

from faq_manager.models import FAQ

# Create your views here.


class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")
        cache_key = f"faqs_{lang}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        data = [
            {
                "question": faq.get_translated_question(lang),
                "answer": faq.answer
            }
            for faq in faqs
        ]
        cache.set(cache_key, data, timeout=300)  # Cache for 5 minutes

        return Response(data)
