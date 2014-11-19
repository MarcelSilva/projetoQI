from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessoas.views',
                       
    url(r'^$', 'index'),
    url(r'^validar/$', 'validar'),
    url(r'^cadastrar/$', 'cadastrar'),
)