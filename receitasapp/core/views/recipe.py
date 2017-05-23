from rest_framework import generics
from rest_framework.views import APIView
from core.models import Recipe
from core.serializers import RecipeThinSerializer, RecipeSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class RecipeList(generics.ListAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeThinSerializer


class RecipeCreate(generics.CreateAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)