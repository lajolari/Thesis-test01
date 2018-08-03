from rest_framework import routers
from search.viewsets import RecetaViewSet, IngredienteViewSet
router = routers.DefaultRouter()
router.register(r'addreceta', RecetaViewSet)
router.register(r'addingrediente', IngredienteViewSet)