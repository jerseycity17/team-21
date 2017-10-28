from django.conf.urls import url

from . import views

app_name = 'ishar'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^IntegratedHealth/$', views.int_health, name='int_health'),
    url(r'^IntegratedCulture/$', views.int_culture, name='int_culture'),
    url(r'^JournalPortal/$', views.journal_portal, name='journal'),
    url(r'^Cosmology/$', views.cosmology, name='cosmology'),
    url(r'^Contact/$', views.contact, name='contact'),
    url(r'^Affilliates/$', views.affilliates, name='affilliates'),
    url(r'^Article/(?P<article_id>[0-9]+)/$', views.article_desc, name='article_desc'),
    url(r'^Category/(?P<category>[^\s]+)/Articles/$', views.article_list, name='article_list'),
    url(r'^Category/(?P<category>[^\s]+)/$', views.category, name='category'),
    url(r'^Mission/$', views.mission, name='mission'),
    url(r'^SupervisingBoard/$', views.super_board, name='super_board'),
    url(r'^BMHJournal/$', views.bmh_journal, name='bmh_journal'),
    url(r'^Consciousness/$', views.consciousness, name='consciousness'),
    url(r'^Consciousness/The_Hard_Problem/$', views.hard_problem, name='hard_problem'),
    url(r'^Consciousness/Philosophy_of_Mind/$', views.philosophy_mind, name='philosophy_mind'),
    url(r'^Consciousness/The_Brain/$', views.brain, name='brain'),
    url(r'^Consciousness/The_Mind/$', views.mind, name='mind'),
    url(r'^Search/$', views.search, name='search')

]