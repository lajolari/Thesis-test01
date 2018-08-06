from django.shortcuts import render
from .models import TipoReceta, Receta, Ingrediente, RecipeStep, Unit, IngredientQuantity
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

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

class AddRecetasView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = Receta
    template_name ='search/addrecetas.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Receta.objects.filter(nombre=self.request.user)   

class RecetaDetailView(generic.DetailView):
    model = Receta
    template_name = 'search/receta_detalle.html'

class AddIngredientesView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = Ingrediente
    template_name ='search/addingredientes.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Ingrediente.objects.filter(nombre=self.request.user)   