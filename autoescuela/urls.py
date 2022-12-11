from django.urls import re_path as url
from django.views.generic import RedirectView
from .views import RegistrarUsuario,index,PermisosListView,IndexExamenListView,PregruntasListView,UsuarioView
from django.urls import include, path


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^permisos/$', PermisosListView.as_view(), name='permisos'),
    url(r'^aula_virtual/$', IndexExamenListView.as_view(), name='aula_virtual'),
    url(r'^preguntas/(?P<pk>\d+)/$', PregruntasListView.as_view(), name='aula_virtual'),
]
urlpatterns += [url(r'^perfil_aula/$', UsuarioView.as_view(), name='perfil_aula'),]
urlpatterns += [url(r'^administracion/$', RegistrarUsuario.as_view(), name='administracion'),]


