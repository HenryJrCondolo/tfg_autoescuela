from django.contrib import admin
from .models import Tema, Permiso, Pregunta, Usuario, Examen, Examen_Usuario

# Register your models here.

admin.site.register(Tema)
admin.site.register(Permiso)
admin.site.register(Pregunta)
admin.site.register(Usuario)
admin.site.register(Examen)
admin.site.register(Examen_Usuario)