from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets

from pizza.models import Pizza, PizzaTopping, Topping
from api.serializers import UserSerializer, PizzaSerializer, PizzaToppingSerializer, ToppingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaToppingViewSet(viewsets.ModelViewSet):
    queryset = PizzaTopping.objects.all()
    serializer_class = PizzaToppingSerializer


class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
