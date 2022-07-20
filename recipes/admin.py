from django.contrib import admin
from recipes.models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    pass

# Register your models here.


admin.site.register(Recipe, RecipeAdmin)
