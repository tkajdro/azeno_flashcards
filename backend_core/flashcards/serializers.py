from rest_framework.serializers import ModelSerializer

from .models import Flashcard, Deck


class FlashcardSerializer(ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'question', 'answer', 'author', 'category', 'difficulty', 'rating', 'tags', 'decks')


class DeckSerializer(ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'category', 'difficulty', 'rating', 'tags', 'name', 'description', 'is_public', 'author')
