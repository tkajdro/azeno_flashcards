from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views, viewsets

app_name = 'flashcards'

router = DefaultRouter()
router.register('decks', viewsets.DeckViewSet, basename='decks')

urlpatterns = [
    path('flashcards/', views.FlashcardView.as_view(), name='flashcards'),
    path('flashcards/<int:rating>', views.FlashcardView.as_view(), name='flashcards'),
    path('flashcards/<int:pk>/', views.FlashcardItemView.as_view(), name='flashcard'),
    *router.urls,
]

# urlpatterns += router.urls
