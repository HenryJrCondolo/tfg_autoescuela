from django.urls import re_path as url
from django.views.generic import RedirectView
from . import views
from django.urls import include, path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^examenes/$', views.ExamenesListView.as_view(), name='examen'),
    url(r'^permisos/$', views.PermisosListView.as_view(), name='permisos'),
]
urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]
