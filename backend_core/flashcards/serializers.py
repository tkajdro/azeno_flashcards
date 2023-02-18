from rest_framework.serializers import ModelSerializer

from .models import Flashcard

class FlashcardSerializer(ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'question', 'answer', 'author', 'category', 'difficulty', 'rating', 'tags', 'decks')
