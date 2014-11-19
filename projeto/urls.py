from django.conf.urls import patterns, include, url

urlpatterns = patterns('pessoas.views',
                       
    url(r'^$', 'index'),
    url(r'^cadastro/$', 'cadastro'),
    url(r'^validar/$', 'validar'),
    
)

    
