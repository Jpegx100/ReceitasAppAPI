from rest_framework import serializers
from core.models import *

#---------Serializers for User---------

class UserThinSeralizer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')

#----Serializers for IngredientType----

class IngredientTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = IngredientType
		fields = ('__all__')

#----Serializers for Ingredient----

class IngredientSerializer(serializers.ModelSerializer):
	quantity = serializers.DecimalField(max_digits=20, decimal_places=4)
	recipe = serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = Ingredient
		fields = ('__all__')

#-------Serializers for Comment-------

class CommentSerializer(serializers.ModelSerializer):
	user = UserThinSeralizer()
	class Meta:
		model = Comment
		fields = ('id', 'text', 'recipe', 'user')

#-------Serializers for Feel-------

class FeelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feel
		fields = ('__all__')

#-------Serializers for Recipe--------

class RecipeSerializer(serializers.ModelSerializer):
	ingredients = IngredientSerializer(many=True)
	feels = FeelSerializer(many=True, read_only=True)
	user = UserThinSeralizer(read_only=True)

	class Meta:
		model = Recipe
		fields = ('id', 'title', 'description', 'how_to_do', 'picture', 'feels', 'ingredients', 'user')

	def create(self, validated_data):
		ingredients = validated_data.pop('ingredients')
		print(ingredients)
		recipe = Recipe.objects.create(**validated_data)
		for ingredient in ingredients:
			Ingredient.objects.create(recipe=recipe, **ingredient)
		return recipe

class RecipeThinSerializer(serializers.ModelSerializer):
	"""
	Thin represetation of Recipe, including just the indispensable attributes.
	"""
	user = UserThinSeralizer(read_only=True)
	feels = FeelSerializer(many=True, read_only=True)
	class Meta:
		model = Recipe
		fields = ('id', 'title', 'description', 'picture', 'feels', 'user')