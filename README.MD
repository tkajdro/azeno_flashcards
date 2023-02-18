# Azeno Flashcards

## Algorytm postępowania:

1. Czy potrzebujemy django app?
   1. 'python manage.py startapp <name>'
   2. Dodaj do installed app -> settings.py
2. Analiza czy potrzebujemy dane?
   1. Narysuj ERD diagram na kartce
   2. Implementacja w models.py
   3. 'pathon manage.py makemigrations <app_name>'
   4. 'python manage.py migrate <app_name>'
   5. Unit tests -> pytest
3. Czy potrzebujemy zarządzać tym zasobem z CMS(django admin)?
   1. Rejestrujemy modele w admin.py
2. Czy wystawiamy dane w widoku?
   3. Tworzymy plik serializers.py (format danych)
   4. Unit tests
5. Tworzymy widoki (logikę)
   6. Dobieramy klasę do obsługi widoku [wyszukiwarka widoków](https://www.cdrf.co)
   7. Widok musi zwracać respons lub redirect
   8. Logika uprawnień permissions.py
   8. Unit tests
9. Tworzymy lokalny router
   10. W pliku urls.py tworzymy urlpatterns lub router
   11. Podpinamy lokalne urls do globalnych urls -> config/urls.py
   12. Unit tests
13. Postman i stworzenie kolekcji
    14. Wyeksportowanie kolekcji do repozytorium