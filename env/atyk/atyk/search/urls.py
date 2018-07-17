from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ingredientes/$', views.IngredienteListView.as_view(), name='ingredientes'),
    url(r'^recetas/$', views.RecetaListView.as_view(), name='recetas'),
    url(r'^receta/(?P<pk>\d+)$', views.RecetaDetailView.as_view(), name='detalle-receta'),
]
urlpatterns += [   
    url(r'^addrecetas/$', views.AddRecetasView.as_view(), name='addrecetas'),
]