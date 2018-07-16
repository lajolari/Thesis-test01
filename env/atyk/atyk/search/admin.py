from django.contrib import admin
from .models import TipoReceta, Receta, Ingrediente, RecipeStep, Unit, IngredientQuantity

admin.site.register(TipoReceta)
admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(RecipeStep)
admin.site.register(Unit)
admin.site.register(IngredientQuantity)

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ingredientes', 'preparacion', 'tipo', 'tiempo_preparacion', 'metodo_coccion', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
# Register your models here.
