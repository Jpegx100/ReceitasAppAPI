from django.db import models
from django.contrib.auth.models import User
from core.utils import *

class Recipe(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	how_to_do = models.CharField(max_length=1000)
	user = models.ForeignKey(User, related_name='recipes')
	picture = models.ImageField(upload_to='pictures', max_length=254, null=True, blank=True)
	creation_date = models.DateTimeField(auto_now_add=True)

class IngredientType(models.Model):
	name = models.CharField(max_length=50, unique=True)

class Ingredient(models.Model):
	quantity = models.DecimalField(max_digits=20, decimal_places=4)
	measurement_unit = models.CharField(max_length=2, choices=MEASUREMENTUNITS)
	ingredient_type = models.ForeignKey(IngredientType, related_name='ingredients')
	recipe = models.ForeignKey(Recipe, related_name='ingredients')

class Comment(models.Model):
	text = models.CharField(max_length=200)
	user = models.ForeignKey(User, related_name='comments')
	recipe = models.ForeignKey(Recipe, related_name='comments')
	creation_date = models.DateTimeField(auto_now_add=True)

class Feel(models.Model):
	value = models.BooleanField()
	user = models.ForeignKey(User, related_name='feels')
	recipe = models.ForeignKey(Recipe, related_name='feels')