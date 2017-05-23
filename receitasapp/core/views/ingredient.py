from rest_framework import generics
from rest_framework.views import APIView
from core.models import Ingredient
from core.serializers import IngredientSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class IngredientList(generics.ListAPIView):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer


class IngredientCreate(generics.CreateAPIView):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer