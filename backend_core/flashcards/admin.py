from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.DifficultyLevel)
admin.site.register(models.Tag)
admin.site.register(models.Deck)
admin.site.register(models.Flashcard)

