from django.shortcuts import render
from .models import TipoReceta, Receta, Ingrediente, RecipeStep, Unit, IngredientQuantity
from django.views import generic

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    recetas=Receta.objects.all().count()
    ingredientes=Ingrediente.objects.all().count()
    # Libros disponibles (status = 'a')
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'recetas':recetas,'ingredientes':ingredientes},
    )

class IngredienteListView(generic.ListView):
    model = Ingrediente

class RecetaListView(generic.ListView):
    model = Receta

# class IngredienteListDetail(generic.ListView):
    
