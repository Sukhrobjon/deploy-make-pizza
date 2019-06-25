from rest_framework import serializers
from pizza.models import PizzaTopping, Pizza, Topping
from django.contrib.auth.models import User


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name',)


class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingSerializer(read_only=True, many=True)

    class Meta:
        model = Pizza
        fields = '__all__'


class PizzaToppingSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer(read_only=True, many=True)
    topping = ToppingSerializer(read_only=True, many=True)

    class Meta:
        model = PizzaTopping
        fields = ('pizza', 'topping')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
