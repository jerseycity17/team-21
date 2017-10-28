from django.conf.urls import url

from . import views

app_name = 'ishar'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^IntegratedHealth/$', views.int_health, name='int_health'),
    #url(r'^/IntegratedCulture/$', views.int_culture, name='int_culture'),
    #url(r'^/JournalPortal/$', views.journal_portal, name='journal'),
    url(r'^Cosmology/$', views.cosmology, name='cosmology'),
    url(r'^Contact/$', views.contact, name='contact'),

]