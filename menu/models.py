from django.contrib import admin
from django.db import models

class Ingredient(models.Model):
    nom = models.CharField(max_length=100)
    importance = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_ingredient_name')
        ]       

class Allergene(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_allergene_name')
        ]

class Entree(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField(default=0)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_entree_name')
        ]

class Pizza(models.Model):
    nom = models.CharField(max_length=100)
    ingredient = models.ManyToManyField(Ingredient)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)
    suggestion = models.BooleanField(default=False)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def get_ingredients(self):
        return ",\n".join([p.nom for p in sorted(self.ingredient.all(),key=lambda ingr: ingr.importance, reverse=True)])

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_pizza_name')
        ]

class Pates(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField(default=0)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_pates_name')
        ]
        verbose_name_plural  =  "Pates"

class Dessert(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField(default=0)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_dessert_name')
        ]

class Boisson(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField(default=0)
    allergene = models.ManyToManyField(Allergene, blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nom'], name='unique_boisson_name')
        ]