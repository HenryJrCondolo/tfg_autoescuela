from django.shortcuts import render
from .models import Usuario, Permiso, Examen_Usuario, Examen, Pregunta, Tema
from django.utils import timezone
from django.views.generic.list import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
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
    permission_required = 'autoescuela.view_permiso'
    model = Permiso
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permiso_list'] = Permiso.objects.all()
        return context
    template_name = 'permisos.html/'
    
class IndexExamenListView(ListView):
    model = Examen
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['examen_list'] = Examen.objects.all
        return context
    template_name = 'aula_virtual.html/'

