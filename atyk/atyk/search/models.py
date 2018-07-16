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
    
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre de un ingrediente (ejemplo: papa, nata, batata)")

    ingredientes = models.ForeignKey('Ingrediente', on_delete=models.SET_NULL, null=True) 

    preparacion = models.TextField(max_length=1000, help_text="Ingrese la preparacion")

    tipo = models.ManyToManyField(TipoReceta, help_text="Seleccione un tipo de receta")

    tiempo_preparacion = models.CharField(max_length=50, help_text="Ingrese el tiempo de preparacion promedio")

    metodo_coccion = models.CharField(max_length=50, help_text="Ingrese un metodo de coccion para la receta principal")

    def __str__(self):
        """
        Cadena que representara la instancia de este modelo
        """
        return self.nombre    
    
    # def get_absolute_url(self):
    #     """
    #     Devuelve el URL a una instancia particular de Receta
    #     """
    #     return reverse('detalle-receta', args=[str(self.id)])

class Ingrediente(models.Model):
    """
    Modelo que representara las caracteristicas de los Ingredientes en el sistema
    """
    nombre = models.CharField(max_length=50)

    reino = models.CharField(max_length=20)

    TIPO_ALIMENTO = (
        ('p', 'Proteina'),
        ('c', 'Carbohidrato'),
        ('m', 'Mineral'),
        ('g', 'Grano'),
        ('ci', 'Citrico'),
        ('d', 'Dulce'),
        ('n', 'Neutro'),
        ('l', 'Lacteo'),
    )

    propiedad_principal = models.CharField(max_length=20, choices=TIPO_ALIMENTO, help_text='Caracteristica del alimento') #Representa la propiedad principal: Si es Proteina, si es Carbohidrato, etc...

    propiedad_secundaria = models.TextField(max_length=500) #Representa todas las propiedades secundarias

    presentacion = models.CharField(max_length=50) #Representa su presentacion para la receta: Pure, crema, solido, liquido, granulado, etc...

    subproducto = models.BooleanField(default=False) #Determina si es un subproducto o no, de ser True, crea un link a la sub-preparacion con sus respectivos ingredietnes y procedimientos (receta)
    
    excepciones = models.CharField(max_length=50, null=True, blank=True) #Excepciones para contrastar (tipo, no usar pure de  tomate en una torta (why not? podria funcionar *thinking*))

    restricciones = models.CharField(max_length=40, null=True, blank=True) #Restricciones de uso, como "no apto para celiacos" and shizzzz...
    #En algun momento, agregar informacion adicional para el usuario, como propiedades nutricionales, peso calorico, restricciones

    def __str__(self):
        """Cadena que representara la instancia de este modelo
        """
        return self.nombre

    # def get_absolute_url(self):
    #     """
    #     Devuelve el URL a una instancia particular de Ingrediente
    #     """
    #     return reverse('detalle-ingrediente', args=[str(self.id)])

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