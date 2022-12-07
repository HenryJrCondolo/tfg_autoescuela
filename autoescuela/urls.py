from django.urls import re_path as url
from django.views.generic import RedirectView
from . import views
from django.urls import include, path


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^permisos/$', views.PermisosListView.as_view(), name='permisos'),
    url(r'^aula_virtual/$', views.IndexExamenListView.as_view(), name='aula_virtual'),
]

