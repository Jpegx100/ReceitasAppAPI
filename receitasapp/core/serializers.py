from rest_framework import serializers
from core.models import *

#---------Serializers for User---------

class UserThinSeralizer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')

class UserSeralizer(serializers.ModelSerializer):

	def create(self, validated_data):
		user = User.objects.create(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user

	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'email')

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
class Base64ImageField(serializers.ImageField):

	def to_internal_value(self, data):
		from django.core.files.base import ContentFile
		import base64
		import six
		import uuid

		if isinstance(data, six.string_types):
			if 'data:' in data and ';base64,' in data:
				header, data = data.split(';base64,')
			try:
				decoded_file = base64.b64decode(data)
			except TypeError:
				self.fail('invalid_image')
			file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
			file_extension = self.get_file_extension(file_name, decoded_file)
			complete_file_name = "%s.%s" % (file_name, file_extension, )
			data = ContentFile(decoded_file, name=complete_file_name)
		return super(Base64ImageField, self).to_internal_value(data)

	def get_file_extension(self, file_name, decoded_file):
		import imghdr
		extension = imghdr.what(file_name, decoded_file)
		extension = "jpg" if extension == "jpeg" else extension
		return extension

	def to_representation(self, value):
		import base64
		if not value:
			return None
		image = open(value.path, 'rb')
		image_base64 = base64.b64encode(image.read())
		return image_base64

class RecipeSerializer(serializers.ModelSerializer):
	ingredients = IngredientSerializer(many=True)
	feels = FeelSerializer(many=True, read_only=True)
	user = UserThinSeralizer(read_only=True)
	picture = Base64ImageField(
    	    max_length=None, use_url=True,
    	)

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
	Thin represetation of Recipe, including just the undispensable attributes.
	"""
	user = UserThinSeralizer(read_only=True)
	feels = FeelSerializer(many=True, read_only=True)
	class Meta:
		model = Recipe
		fields = ('id', 'title', 'description', 'picture', 'feels', 'user')