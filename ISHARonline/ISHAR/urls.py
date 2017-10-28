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
    url(r'^(?P<category>[a-z]+)/Articles/$', views.article_list, name='article_list'),
    url(r'^(?P<category>[a-z]+)/$', views.category, name='category'),
    url(r'^Mission/$', views.mission, name='mission'),
    url(r'^SupervisingBoard/$', views.super_board, name='super_board'),
    url(r'^bmhJournal/$', views.bmh_journal, name='bmh_journal'),


]