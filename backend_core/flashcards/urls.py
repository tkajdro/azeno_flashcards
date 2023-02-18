from django.urls import path

from . import views

app_name = 'flashcards'

urlpatterns = [
    path('flashcards/', views.FlashcardView.as_view(), name='flashcards'),
    path('flashcards/<int:rating>', views.FlashcardView.as_view(), name='flashcards'),
    path('flashcards/<int:pk>/', views.FlashcardItemView.as_view(), name='flashcard'),
]