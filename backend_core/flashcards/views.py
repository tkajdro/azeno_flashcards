from rest_framework.generics import ListAPIView
from .models import Flashcard
from .serializers import FlashcardSerializer

class FlashcardView(ListAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
