from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)


class Unit(models.Model):
    name = models.CharField(max_length=255)


class Meal(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    recipe= models.TextField()


class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.Integer()
    unit = models.ForeignKey(Unit)
