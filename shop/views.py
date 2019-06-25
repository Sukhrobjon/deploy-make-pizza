
from django.shortcuts import render, Http404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def home(request):
    return render(request, 'shop/home.html', {
    })
