from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse

from .models import Article, Category, SubCategory

def index(request):
	return render(request, 'ISHAR/index.html', {})

def int_health(request):
	category_list = Category.objects.all()
	sub_category_list = SubCategory.objects.all()
	return render(request, 'ISHAR/intHealth.html', {'category_list' : category_list,
													'sub_category_list': sub_category_list})

def int_culture(request):
	return render(request, 'ISHAR/intCulture.html', {})

def cosmology(request):
	return render(request, 'ISHAR/compWorldCosmologies.html', {})

def contact(request):
	return render(request, 'ISHAR/contact.html', {})

def affilliates(request):
	return render(request, 'ISHAR/affilliates.html', {})

def article_desc(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	return render(request, 'ISHAR/articleDesc.html', {'article' : article})

def article_list(request, category):
	article_list = get_list_or_404(Article, category__category_name=category)[:10]
	return render(request, 'ISHAR/articleList.html', {'article_list': article_list})

def category(request, category):
	return render(request, 'ISHAR/categoryDesc.html', {'category' : category})

def mission(request):
	return render(request, 'ISHAR/mission.html', {})

def super_board(request):
	return render(request, 'ISHAR/supervisingBoard.html', {})

def journal_portal(request):
	return render(request, 'ISHAR/journalPortal.html', {})

def bmh_journal(request):
	return render(request, 'ISHAR/bmhJournal.html', {})

def consciousness(request):
	return render(request, 'ISHAR/Consciousness.html', {})

def hard_problem(request):
	return render(request, 'ISHAR/consciousness-hardProb.html', {})

def philosophy_mind(request):
	return render(request, 'ISHAR/consciousness-philMind.html', {})

def brain(request):
	return render(request, 'ISHAR/consciousness-brain.html', {})

def mind(request):
	return render(request, 'ISHAR/consciousness-mind.html', {})




