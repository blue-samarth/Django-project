from ckeditor.fields import RichTextField
from googletrans import Translator
import logging

from django.db import models

logger : logging.Logger = logging.getLogger(__name__)
# Create your models here.
class FAQ(models.Model):
    """
    FAQ (Frequently Asked Questions) model that supports multilingual content.

    Attributes:
        question (TextField): The FAQ question in English
        answer (RichTextField): The answer with WYSIWYG editor support
        question_hi (TextField): Hindi translation of the question (auto-generated)
        question_bn (TextField): Bengali translation of the question (auto-generated)
        created_at (DateTimeField): Timestamp of FAQ creation

    Methods:
        get_translated_question: Retrieves question in specified language
        save_translate: Handles automatic translation during save
    """

    class Meta:
        """
        Metadata class for FAQ model.
        
        Attributes:
            verbose_name (str): Human-readable singular name ('FAQ')
            verbose_name_plural (str): Human-readable plural name ('FAQs')
            ordering (list): Default ordering by creation date (newest first)
        """
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['-created_at']


    question : models.TextField = models.TextField(help_text = "Question in English")
    answer : RichTextField = RichTextField() # as we are required WYSIWYG editor support
    question_hi : models.TextField = models.TextField(blank=True, null=True, help_text="Hindi translation") 
    question_bn : models.TextField = models.TextField(blank=True, null=True, help_text="Bengali translation")

    created_at = models.DateTimeField(auto_now_add=True)
 
    def get_translated_question(self, lang: str = 'en') -> str:
        """Get question in specified language, fallback to English"""
        if lang == "en" : return self.question
        try:
            translated : str =  getattr(self, f'question_{lang}', self.question)
            return translated if translated else self.question
        except AttributeError:
            return self.question
    
    def save(self, *args, **kwargs) -> None:
        if not self.pk and self.question:
            translator = Translator()
            for lang in ['hi', 'bn']:
                feild_name : str = f'question_{lang}'
                if getattr(self, feild_name) is None :  # Only translate if the field is empty
                    try:
                        translated : Translator.translate = translator.translate(self.question, dest=lang)
                        setattr(self, f'question_{lang}', translated.text)
                    except Exception as e:
                        logger.error(f"Translation failed for {lang} : {str(e)}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.question
