from django.shortcuts import render
from .models import Usuario, Permiso, Examen_Usuario, Examen, Pregunta, Tema

# Create your views here.
def index(request):
    """ 
    Función vista para la página de inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_usuarios = Usuario.objects.all().count()
    num_permisos = Permiso.objects.all().count()
    
    # Número de examenes que han sido realizados por los usuarios
    num_examenes_realizados = Examen_Usuario.objects.all().count()
    num_preguntas = Pregunta.objects.all().count()
    
    #Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request, 'autoescuela/index.html', context={'num_usuarios':num_usuarios,'num_permisos':num_permisos,'num_examenes_realizados':num_examenes_realizados,'num_preguntas':num_preguntas,},)