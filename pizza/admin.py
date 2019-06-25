from django.contrib import admin
from pizza.models import Pizza, PizzaTopping, Topping


admin.site.register(Pizza)
admin.site.register(PizzaTopping)
admin.site.register(Topping)
