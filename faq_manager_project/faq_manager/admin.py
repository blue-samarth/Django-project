from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import FAQ
# Register your models here.


class FAQAdminForm(forms.ModelForm):
    """Custom form to apply CKEditor widget to answer field"""
    answer = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FAQ
        fields = '__all__'  # Include all fields


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """Admin configuration for FAQ model"""
    form = FAQAdminForm
    list_display = ('question', 'created_at')
    search_fields = ('question',)  # It needs to be a Tuple
    list_filter = ('created_at',)

    fieldsets = [
        ('English Content', {'fields': ['question', 'answer']}),  # Main content
        ('Translations', {
            'fields': ['question_hi', 'question_bn'],
            'classes': ('collapse',),  # Collapsed section
        }),
    ]
