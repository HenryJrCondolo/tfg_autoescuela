from django.contrib import admin
from .models import Tema, Permiso, Pregunta, Usuario, Examen, Examen_Usuario

# Register your models here.
from django.contrib import admin
from .models import Tema, Permiso, Pregunta, Usuario, Examen, Examen_Usuario

# Register your models here.

# admin.site.register(Tema)
# Define the admin class


class TemaAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('tema', 'descripcion')
    fields = ['tema', 'descripcion']


# Register the admin class with the associated model
admin.site.register(Tema, TemaAdmin)

# admin.site.register(Permiso)
# Define the admin class


class PermisoAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('tipo_licencia', 'precio')
    fields = ['tipo_licencia', 'descripcion', 'precio']


# Register the admin class with the associated model
admin.site.register(Permiso, PermisoAdmin)

# admin.site.register(Pregunta)
# Define the admin class


class PreguntaAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('permiso', 'tema', 'pregunta', 'respuesta_Correcta','respuesta_Falsa_1', 'respuesta_Falsa_2', 'imagen_pregunta')
    fields = [('permiso', 'tema'), 'pregunta', 'respuesta_Correcta', 'respuesta_Falsa_1','respuesta_Falsa_2', 'imagen_pregunta', 'descripcion_adicional']


# Register the admin class with the associated model
admin.site.register(Pregunta, PreguntaAdmin)

# admin.site.register(Usuario)
# Define the admin class


class UsuarioAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('dni', 'nombre', 'apellidos', 'email', 'telefono', 'direccion', 'fecha_nacimiento', 'fecha_matriculacion', 'fecha_baja', 'permiso', 'imagen_usuario')
    fields = ['dni','nombre', 'apellidos', 'email', 'telefono', 'direccion', 'fecha_nacimiento', 'fecha_matriculacion', 'fecha_baja', 'permiso', 'imagen_usuario']
# Register the admin class with the associated model
admin.site.register(Usuario, UsuarioAdmin)

# admin.site.register(Examen)
# Define the admin class


class ExamenAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('nombre_Examen', 'display_preguntas')
    fields = ['nombre_Examen', 'preguntas']


# Register the admin class with the associated model
admin.site.register(Examen, ExamenAdmin)

# admin.site.register(Examen_Usuario)
# Define the admin class


class Examen_UsuarioAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = ('usuario', 'examen', 'fecha', 'respuestas_Usuario', 'id_preguntas_falladas', 'aprobado')
    fields = ['usuario', 'examen', 'fecha', 'respuestas_Usuario', 'id_preguntas_falladas', 'aprobado']

# Register the admin class with the associated model
admin.site.register(Examen_Usuario, Examen_UsuarioAdmin)