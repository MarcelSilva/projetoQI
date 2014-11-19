from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessoas.views',
    url(r'^$','pessoas.views.index'),
    url(r'^validar/$', 'pessoas.views.validar'),
    url(r'^adicionar/$', 'pessoas.views.adicionar'),
)
