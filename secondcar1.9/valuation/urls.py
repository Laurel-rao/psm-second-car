from django.conf.urls import url
from .views import *

# valuation 应用中的urls.py
urlpatterns = [
    url(r'^$',index_views,name='index'),
    url(r'^\w*[/]?psm$',citycarnum,name='car'),
    url(r'^\w*[/]?page2/$', page2_views),
    url(r'^\w*[/]?about/$', about_views, name='about'),
    url(r'^\w*[/]?ajax_province$', ajax_province),
    url(r'^\w*[/]?ajax_city$', ajax_city),
    url(r'^\w*[/]?ajax_brand$', ajax_brand),
    url(r'^\w*[/]?ajax_style$', ajax_style),
    url(r'^\w*[/]?ajax_model$', ajax_model),
    url(r'^\w*[/]?ajax_year$', ajax_year),
    url(r'^\w*[/]?ajax_month$', ajax_month),
    url(r'^\w*[/]?valuation$', valuation),
    url(r'^\w*[/]?ajax_value$', ajax_value),
    url(r'^\w*[/]?ajax_carcount$', ajax_carcount),
    url(r'^\w*[/]?ajax_pricenum$', ajax_pricenum),
    url(r'^\w*[/]?ajax_sellage$', ajax_sellage),
    url(r'^login/$', login_views, name='login'),
    url(r'^register/$', register_views, name='register'),
]