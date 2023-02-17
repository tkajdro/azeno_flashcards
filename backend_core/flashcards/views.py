from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Flashcard
from .serializers import FlashcardSerializer

class FlashcardView(ListCreateAPIView):
#    queryset = Flashcard.objects.filter(rating__gte=42)
    permission_classes = [IsAuthenticated]
    serializer_class = FlashcardSerializer

    def get_queryset(self):
        rating = self.request.query_params.get('rating', 0)

        return Flashcard.objects.filter(rating__gte=rating)
class FlashcardItemView(RetrieveUpdateDestroyAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

