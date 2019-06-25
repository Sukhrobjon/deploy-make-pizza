from django.db import models


class PizzaTopping(models.Model):
    topping = models.ForeignKey('Topping', on_delete=models.PROTECT)
    pizza = models.ForeignKey('Pizza', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.pizza.name} with {self.topping.name}"


class Pizza(models.Model):
    PIZZA_SIZES = (
        (12, '12in'),
        (18, '18in'),
    )

    name = models.CharField(max_length=60)
    toppings = models.ManyToManyField('Topping', through=PizzaTopping)
    price_small = models.DecimalField(max_digits=8, decimal_places=2)
    price_big = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=60)
    on_top_of = models.ManyToManyField('Pizza', through=PizzaTopping)

    def __str__(self):
        return self.name
