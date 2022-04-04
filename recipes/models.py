from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.enums import IntegerChoices
from django.db.models.fields import BLANK_CHOICE_DASH, IntegerField

# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=32, blank=False)

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poster")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=32, blank=False)
    description = models.CharField(max_length=500, blank=False)
    ingredients =  models.CharField(max_length=300, blank=False)
    preparation = models.CharField(max_length=1000, blank=False)
    tips = models.CharField(max_length=200, blank=True)
    difficulty = models.CharField(max_length=10, blank=False)
    time = models.IntegerField(blank=False)
    cost = models.CharField(max_length=10, blank=True)

class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    recipe = models.ManyToManyField(Recipe, blank=True, related_name="saved")

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")
    value = IntegerField(blank=False)