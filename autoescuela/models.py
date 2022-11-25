from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.
class Tema(models.Model):
    #Esta clase representa los temas de la autoescuela
    id_Tema =  models.AutoField(primary_key=True) #Identificador del tema
    tema = models.CharField(max_length=100) #Nombre del tema
    descripcion = models.TextField() #Descripción del tema
    def __str__(self):
        return "Tema: "+self.tema+"; Descripción: "+self.descripcion
    
class Permiso(models.Model):
    #Esta clase representa a los permisos que se pueden obtener en la autoescuela
    tipo_licencia = models.CharField(primary_key=True, max_length=11, unique=True) #Tipo de licencia A, B, C, D 
    descripcion = models.TextField() #Descripción del permiso
    precio = models.FloatField(null=True, blank=True, default=0.0) #Precio del permiso
    def __str__(self):
        return "Permiso: "+self.tipo_licencia+"; precio: "+str(self.precio)+"; Descripción: "+self.descripcion
     
class Pregunta(models.Model):
    #Esta clase representa a las preguntas de que generan los exámenes
    id_Pregunta = models.AutoField(primary_key=True);
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE) #Relación con la clase Tema (Muchos a uno)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE) #Relación con la clase Permiso (Muchos a uno)
    pregunta = models.TextField()
    respuesta_Falsa_1 = models.TextField()
    respuesta_Falsa_2 = models.TextField()
    respuesta_Correcta = models.TextField()
    imagen_pregunta = models.ImageField(upload_to='preguntas', null=True, blank=True) #Campo para subir imágenes de las preguntas
    descripcion_adicional = models.TextField(null=True, blank=True) #Campo para añadir descripciones adicionales a la respuesta correcta
    def __str__(self):
        return "Pregunta: "+self.pregunta+"; Tema: "+ self.tema.tema+ "; Permiso: "+self.permiso.tipo_licencia + "; Respuesta Correcta: " + self.respuesta_Correcta+"; Respuesta Falsa 1: "+self.respuesta_Falsa_1+"; Respuesta Falsa 2: "+self.respuesta_Falsa_2+"; Descripción adicional: "+self.descripcion_adicional
    
class Usuario(models.Model):
    #Esta clase representa a los usuarios de la autoescuela
    dni = models.CharField(primary_key=True, max_length=11, unique=True) #DNI del usuario
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE, null=False) #Relación con la clase Permiso (Muchos a uno)
    nombre = models.CharField(max_length=100)  #Nombre del usuario
    apellidos = models.CharField(max_length=100) 
    fecha_nacimiento = models.DateField()
    imagen_usuario = models.ImageField(upload_to='usuarios', null=True, blank=True) #Campo para subir imágenes de los usuarios
    direccion = models.CharField(max_length=100) #Dirección del usuario
    telefono = models.CharField(max_length=9) #Teléfono del usuario
    email= models.EmailField()  #Email del usuario
    fecha_matriculacion = models.DateField(null=False) #Fecha de matriculación del usuario
    fecha_baja = models.DateField(default=None, null=True, blank=True) #Fecha de salida del usuario, es decir cuando el usuari apruebe el examen
    def __str__(self):
        return "DNI: "+self.dni + "; Nombre " + self.nombre + " " + self.apellidos+"; Fecha de nacimiento: "+str(self.fecha_nacimiento)+"; Dirección: "+self.direccion+"; Teléfono: "+self.telefono
    
class Examen (models.Model):
    #Esta clase representa a los exámenes que se realizan en la autoescuela
    id_Examen = models.AutoField(primary_key=True) 
    nombre_Examen = models.CharField(max_length=100) #Nombre del examen
    preguntas = models.ManyToManyField(Pregunta) #Relación con la clase Pregunta (Muchos a muchos)
    def __str__(self):
        return "Examen: "+self.nombre_Examen+"; Preguntas: "+"".join(str(seg) for seg in self.preguntas.all())
    def get_absolute_url(self):
        return reverse(self.nombre_Examen, args=[str(self.id_Examen)])
    def display_preguntas(self):
        return ', '.join(pregunta.pregunta for pregunta in self.preguntas.all())
    
    
class Examen_Usuario (models.Model):
    #Esta clase representa a los exámenes realizados por los usuarios en la autoescuela
    id_Examen_Usuario = models.AutoField(primary_key=True)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE) #Relación con la clase Examen (Muchos a uno)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #Relación con la clase Usuario (Muchos a uno)
    respuestas_Usuario = ArrayField(models.TextField(), blank=True, default=None) #Array con las respuestas del usuario
    id_preguntas_falladas = ArrayField(models.TextField(), blank=True, default=None, null=True)  #Array con las preguntas falladas por el usuario
    aprobado = models.BooleanField(default=False) #Booleano que indica si el usuario ha aprobado el examen o no
    fecha = models.DateField(null=False) #Fecha en la que se realiza el examen
        
    def __str__(self):
        return "Examen: "+self.examen+"; Usuario: "+self.usuario+"; Respuestas del usuario: "+self.respuestas_Usuario+"; Preguntas falladas: "+self.preguntas_falladas+"; Aprobado: "+self.aprobado+"; Fecha: "+self.fecha
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})




