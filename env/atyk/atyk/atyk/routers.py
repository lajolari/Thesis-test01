from rest_framework import routers
from search.viewsets import RecetaViewSet
router = routers.DefaultRouter()
router.register(r'addreceta', RecetaViewSet)