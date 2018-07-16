from django.contrib import admin
from .models import TipoReceta, Receta, Ingrediente, RecipeStep, Unit, IngredientQuantity

admin.site.register(TipoReceta)
admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(RecipeStep)
admin.site.register(Unit)
admin.site.register(IngredientQuantity)

# Register your models here.
