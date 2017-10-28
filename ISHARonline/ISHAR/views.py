from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Category

def index(request):
	return render(request, 'ISHAR/index.html', {})

def int_health(request):
	#category_list = Category.objects
	return render(request, 'ISHAR/intHealth.html', {})

def cosmology(request):
	return render(request, 'ISHAR/compWorldCosmologies.html', {})

def contact(request):
	return render(request, 'ISHAR/contact.html', {})
