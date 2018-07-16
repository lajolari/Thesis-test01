from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ingredientes/$', views.IngredienteListView.as_view(), name='ingredientes'),
    url(r'^recetas/$', views.RecetaListView.as_view(), name='recetas'),
    
]