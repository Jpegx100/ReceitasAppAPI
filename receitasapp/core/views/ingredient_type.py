from rest_framework import generics
from rest_framework.views import APIView
from core.models import IngredientType
from core.serializers import IngredientTypeSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class IngredientTypeList(generics.ListAPIView):
	queryset = IngredientType.objects.all()
	serializer_class = IngredientTypeSerializer


class IngredientTypeCreate(generics.ListAPIView):
	queryset = IngredientType.objects.all()
	serializer_class = IngredientTypeSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)


class IngredientTypeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = IngredientType.objects.all()
	serializer_class = IngredientTypeSerializer