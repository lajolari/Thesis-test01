from rest_framework import viewsets
from .models import Receta, Ingrediente
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import RecetaSerializer, IngredienteSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

    @csrf_exempt
    def receta_list(self):
        if self.method == 'GET':
            queryset = Receta.objects.all()
            serializer_class = RecetaSerializer(queryset, many=True)
            return JsonResponse(serializer_class.data, safe = False)

        elif self.method == 'POST':
            data = JSONParser().parse(self)
            serializer_class = RecetaSerializer(data = data)
            if serializer_class.is_valid():
                serializer_class.save()
                return JsonResponse(serializer_class.data, status = 201)
            return JsonResponse(serializer_class.errors, status=400)

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    @csrf_exempt
    def receta_list(self):
        if self.method == 'GET':
            queryset = Ingrediente.objects.all()
            serializer_class = IngredienteSerializer(queryset, many=True)
            return JsonResponse(serializer_class.data, safe = False)

        elif self.method == 'POST':
            data = JSONParser().parse(self)
            serializer_class = IngredienteSerializer(data = data)
            if serializer_class.is_valid():
                serializer_class.save()
                return JsonResponse(serializer_class.data, status = 201)
            return JsonResponse(serializer_class.errors, status=400)