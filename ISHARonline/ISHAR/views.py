from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
	tags = None
	related_articles = None
	try:
		tags = article.tags
		tags = tags[0]
		related_articles = list(Article.objects.filter(tags__contains=tags))[:5]
	except:
		pass
	if tags is None:
		related_articles = list(Article.objects.filter(author__contains=article.author.split(',')[0]))[:5]
	return render(request, 'ISHAR/articleDesc.html', {'article' : article,
													  'related_articles': related_articles})
def article_list(request, category):
	article_list = get_list_or_404(Article, category__category_name=category)
	paginator = Paginator(article_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	
	return render(request, 'ISHAR/articleList.html', {'article_list': articles})

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

def honorarium(request):
	return render(request, 'ISHAR/honorarium.html', {})

def search(request):
	search_param = request.POST['search_param']
	article_list_title = list(Article.objects.filter(title__contains=search_param))
	article_list_author = list(Article.objects.filter(author__contains=search_param))
	article_list_tags = list(Article.objects.filter(tags__contains=search_param))
	article_list_abstract = list(Article.objects.filter(abstract__contains=search_param))
	master_list = list(set().union(article_list_title, article_list_abstract, article_list_tags, article_list_author))


	paginator = Paginator(master_list, 10)

	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	
	return render(request, 'ISHAR/articleList.html', {'article_list': articles})
