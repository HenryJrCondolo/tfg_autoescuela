from django.shortcuts import render
from .models import Usuario, Permiso, Examen_Usuario, Examen, Pregunta, Tema
from django.utils import timezone
from django.views.generic.list import ListView, View
from django.views.generic import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

class PregruntasListView(ListView):
    model = Pregunta
    def get_queryset(self):
        return Pregunta.objects.filter(tema__id=self.kwargs['pk'])
    template_name = 'preguntas_list.html/'

class PermisosListView(PermissionRequiredMixin,ListView):
    permission_required = 'accounts/autoescuela.view_permiso'
    model = Permiso
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permiso_list'] = Permiso.objects.all()
        return context
    template_name = 'permisos.html/'
    
class IndexExamenListView(PermissionRequiredMixin,ListView):
    permission_required = 'autoescuela.view_examen'
    model = Examen
    template_name = 'aula_virtual.html/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['examen_list'] = Examen.objects.all
        return context
    
class ExamenUsuarioListView(LoginRequiredMixin,ListView):
    model = Examen_Usuario;
    template_name = 'perfil_aula.html/'
    permission_required = 'autoescuela.view_examen_usuario'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['examen_usuario_list'] = Examen_Usuario.objects.filter(usuario=self.request.user.dni)
        return context


class UsuarioView(LoginRequiredMixin,View):
    PermissionRequiredMixin = 'autoescuela.view_examen'
    def get(self, request, *args, **kwargs):
        usuario = Usuario.objects.get(dni=self.request.user.dni)
        return render(request, 'perfil_aula.html', {'usuario': usuario})

class RegistrarUsuario(PermissionRequiredMixin,CreateView):
    permission_required = 'autoescuela.add_usuario'
    model = Usuario
    fields = ['dni','nombre','apellidos','email','telefono','direccion','fecha_nacimiento','permiso']
    template_name = 'administracion.html/'
    success_url = '/administracion/'

