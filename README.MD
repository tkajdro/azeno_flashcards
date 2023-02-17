# Azeno Flashcards

## Algorytm postępowania

1. Czy potrzebujemy django app?
   1. 'python manage.py startapp <nazwa>'
   2. dodaj do INSTALLED_APPS -> settings.py
2. Analiza czy potrzebujemy dane?
   1. narysuj diagram na kartce (ERD)
   2. implementacja w models.py
   3. 'python manage.py makemigrations <nazwa>'
   4. 'python manage.py migrate <nazwa>'
   5. Unit tests -> pytest
3. Czy potrzebujemy zarządzać tym zasobem z CMS (django admin)?
   1. Rejestrujemy modele w admin.py
4. Czy wystawiamy dane w widoku?
   1. Tworzymy plik serializers.py
   2. Unit tests
5. Tworzymy widoki (logikę)
   1. Dobieramy odpowiednią klasę do obsługi widoku [wyszukiwarka widowków](https://www.cdrf.co)
   2. Widok musi zwracać response lub redirect
   3. Logika uprawnień permissions.py
   4. Unit tests
6. Tworzymy lokalny router
   1. W pliku urls.py tworzymu urlspatterns lub router
   2. Podpinamy lokalne urls do globalnych urls -> config/urls.py
   3. Unit tests
7. Postman i stworzenie kolekcji
   1. Wyeksportowanie kolekcji do repozytorium 
