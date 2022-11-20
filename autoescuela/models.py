from django.db import models

# Create your models here.
class Temas(models.Model):
    #Esta clase representa los temas de la autoescuela
    id_Tema = models.AutoField(primary_key=True);
    tema = models.CharField(max_length=100)
    descripcion = models.TextField()
    def __str__(self):
        return "Tema: "+self.nombre + "; Descripción " + self.descripcion

class Permiso(models.Model):
    #Esta clase representa a los permisos que se pueden obtener en la autoescuela
    id_Permiso = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_Permiso_Usuario = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre
 
class Pregunta(models.Model):
    #Esta clase representa a las preguntas de que generan los exámenes
    id_Pregunta = models.AutoField(primary_key=True);
    tema = models.ForeignKey(Temas, on_delete=models.CASCADE)
    pregunta = models.TextField()
    respuesta_Falsa_1 = models.TextField()
    respuesta_Falsa_2 = models.TextField()
    respuesta_Correcta = models.TextField()
    imagen_pregunta = models.ImageField(upload_to='preguntas', null=True, blank=True)
    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    #Esta clase representa a los usuarios de la autoescuela
    dni = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    def __str__(self):
        return self.nombre

class usuario_permiso(models.Model):
    #Esta clase representa los permisos de los usuarios
    id_permiso = models.AutoField(primary_key=True)
    fecha_matricula = models.DateField()
    fecha_salida = models.DateField()
    dni = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)
    def __str__(self):
        return "Permiso: "+self.id_Tema + "; Fecha expedición " + self.fecha_expedicion + "; Fecha caducidad " + self.fecha_caducidad
    
class Examen (models.Model):
    #Esta clase representa a los exámenes que se realizan en la autoescuela
    id_Examen = models.AutoField(primary_key=True)
    nombre_Examen = models.CharField(max_length=100)
    preguntas = models.ManyToManyField(Pregunta)
    def __str__(self):
        return self.nombre
    
class Examen_Usuario (models.Model):
    #Esta clase representa a los exámenes realizados por los usuarios en la autoescuela
    id_Examen_Usuario = models.AutoField(primary_key=True)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    respuestas_Usuario = models.ArrayField(models.TextField())
    preguntas_falladas = models.ArrayField(models.ForeignKey(Pregunta, on_delete=models.CASCADE));
    aprobado = models.BooleanField(default=False)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nombre





