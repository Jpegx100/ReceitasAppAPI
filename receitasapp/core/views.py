from django.shortcuts import render
from core.serializers import *
from rest_framework import generics


class RecipeList(generics.ListCreateAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeThinSerializer
	
	def get_serializer_class(self):
		if self.request.method == 'GET':
			return self.serializer_class
		elif self.request.method == 'POST':
			return RecipeSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

class IngredientTypeList(generics.ListCreateAPIView):
	queryset = IngredientType.objects.all()
	serializer_class = IngredientTypeSerializer

class IngredientTypeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = IngredientType.objects.all()
	serializer_class = IngredientTypeSerializer

class IngredientList(generics.ListCreateAPIView):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	
	def perform_update(self, serializer):
		serializer.save(user=self.request.user)

class FeelList(generics.ListCreateAPIView):
	queryset = Feel.objects.all()
	serializer_class = FeelSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class FeelDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Feel.objects.all()
	serializer_class = FeelSerializer

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)
