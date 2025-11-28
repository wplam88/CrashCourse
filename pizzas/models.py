from django.db import models

class Pizza(models.Model):
    """Pizza types"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """Retuns a string representation of the model"""
        return self.name

class Topping(models.Model):
    """Toppings on created pizzas"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        """Return a simple string representing the pizza toppings"""
        return self.name


