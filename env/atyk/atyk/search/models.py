from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class TipoReceta(models.Model):
    """
    Modelo que representara las Categorias de la Receta
    """
    categoria = models.CharField(max_length=20, help_text="Ingrese la categoria de la receta")

    def __str__(self):
        """
        Cadena que representara la instancia de este modelo
        """
        return self.categoria

class Receta(models.Model):
    """
    Modelo que representara las Recetas en el sistema
    """
    # id = models.AutoField(primary_key=True, default=1, help_text="ID único para esta receta particular en toda la biblioteca")

    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre de un ingrediente (ejemplo: papa, nata, batata)")

    ingredientes = models.TextField(max_length=1000) 

    preparacion = models.TextField(max_length=1000, help_text="Ingrese la preparacion")

    tipo = models.CharField(max_length=20, help_text="Ingrese un tipo de Receta", default='Desayuno' )

    tiempo_preparacion = models.CharField(max_length=50, help_text="Ingrese el tiempo de preparacion promedio")

    metodo_coccion = models.CharField(max_length=50, help_text="Ingrese un metodo de coccion para la receta principal")


    def __str__(self):
        """
        Cadena que representara la instancia de este modelo
        """
        return self.nombre   
    
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Receta
        """
        return reverse('detalle-receta', args=[str(self.id)])

class Ingrediente(models.Model):
    """
    Modelo que representara las caracteristicas de los Ingredientes en el sistema
    """
    nombre = models.CharField(max_length=50)

    sustituiblex = models.CharField(max_length=200)

    def __str__(self):
        """Cadena que representara la instancia de este modelo
        """
        return self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Ingrediente
        """
        return reverse('detalle-ingrediente', args=[str(self.id)])

class RecipeStep(models.Model):
    class Meta:
        default_related_name = 'recipe_step_set'

    number  = models.PositiveSmallIntegerField(null=True, blank=True)
    content = models.TextField()
    recipe  = models.CharField('Receta', max_length=100)

    def __str__(self):
        """
        Cadena que representara la instancia de este modelo
        """
        return self.recipe

class Unit(models.Model):
    class Meta:
        ordering = ['long_name']

    long_name  = models.CharField(max_length=60, unique=True)
    short_name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        """
        Cadena que representara la instancia de este modelo
        """
        return self.long_name

class IngredientQuantity(models.Model):
    class Meta:
        default_related_name = 'ingredient_quantity_set'
        verbose_name_plural  = 'recipe ingredient quantities'

    # Modeled as a string so we can do things like "1-2"
    measure = models.CharField(max_length=10, null=True, blank=True)
    unit = models.ForeignKey('Unit', on_delete=models.SET_NULL, null=True, blank=True)

    ingredient  = models.ForeignKey('Ingrediente', on_delete=models.PROTECT)
    
    recipe = models.CharField('Receta', max_length=100)

    def __str__(self):
        """
        Cadena que representara la instancia de este modelo
        """
        return self.measure

