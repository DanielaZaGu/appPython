from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos

# Create your models here.
# Crear la estructura de la aplicación en el modelo de datos:

#Modelo de la tabla Roles:
class Roles(models.Model):
    RoleName = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "perfiles"

    #Crea la función para llamar atributos:
    def __str__(self):
        return self.RoleName

#Modelo de la tabla DatosUser:
class DatosUser(models.Model):
    userDNI = models.CharField(max_length = 20, verbose_name= "identificación")
    nombUser = models.CharField(max_length = 200, null=True, verbose_name= "Nombres")
    apelUser = models.CharField(max_length = 200, null=True, verbose_name= "Apellidos")
    profeUser = models.CharField(max_length = 100, null=True, verbose_name= "Profesión")
    fotoUser = models.ImageField(default='user.png', verbose_name = "Foto de perfil", upload_to="perfiles/img")
    teleUser = models.CharField(max_length = 20,  verbose_name = "Número de telefono")
    geneUser = models.CharField(max_length = 20, choices = Generos, default = " Otro", verbose_name= "Genero")
    adddata = models.DateTimeField(auto_now_add = True, null=True, auto_now = False, verbose_name= "Creado el")
    modiflat = models.DateTimeField(auto_now = True, null = True, verbose_name= "Modificado el")
    
    class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Información"


    #Crea la función para llamar atributos:
    def __str__(self):
        return self.nombUser

#Modelo de la tabla Habilidades:
class Habilidades(models.Model):
    NombHabil = models.CharField(max_length = 155)
    DescHabil = models.TextField(max_length = 2000, verbose_name =  "Decripción de la Habilidad")

    class Meta:
        verbose_name = "Habilidades del Usuario"
        verbose_name_plural = "Competencias"

    #Crea la función para llamar atributos:
    def __str__(self):
        return self.NombHabil

#Modelo de la tabla Detalle Rol:
class DetaRoles(models.Model):
    idRole = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name =  "Identificador de Rol")
    idUser = models.ForeignKey(DatosUser, on_delete=models.CASCADE)
    addUser = models.DateTimeField(auto_now_add = True, auto_now = False, null=True)
    udtUser = models.DateTimeField(auto_now = True)
    estaRol = models.CharField(max_length = 10)

    class Meta:
        verbose_name = "Roles de Usuario"
        verbose_name_plural = "Roles"
   
    #Función de selección:
    def __str__(self):
        return self.idUser


#Modelo de la tabla Rates:
class Rates(models.Model):
    idHabil = models.ForeignKey(Habilidades, on_delete=models.CASCADE)
    idUser = models.ForeignKey(DatosUser, on_delete=models.CASCADE)
    pcrHabil = models.DecimalField(max_digits = 2, decimal_places = 1)
    udtHabil = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Nivel de Habilidad"
        verbose_name_plural = "Niveles de Usuario"
   
    #Función de selección:
    def __str__(self):
        return self.idUser