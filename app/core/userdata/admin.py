from django.contrib import admin
#Importamos las clases desde los modelos:
from .models import Roles, DatosUser, Habilidades, DetaRoles, Rates

# Register your models here.

#Registro del modelo de Roles
class RoleModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    list_display_links = ["RoleName"]
    list_filter = ["RoleName"]

    class Meta:
        model = Roles

admin.site.register(Roles)

#Registro del modelo de DatosUser
class DatosUserModel(admin.ModelAdmin):
    list_display = ["nombUser", "apelUser"]
    list_display_links = ["nombUser"]
    list_filter = ["nombUser"]

    class Meta:
        model = DatosUser

admin.site.register(DatosUser)

#Registro del modelo de Habilidades
class HabilidadesModel(admin.ModelAdmin):
    list_display = ["NombHabil"]
    list_display_links = ["NombHabil"]
    list_filter = ["NombHabil"]

    class Meta:
        model = Habilidades

admin.site.register(Habilidades)

#Registro del modelo de DetaRoles
class DetaRolesModel(admin.ModelAdmin):
    list_display = ["idUser"]
    list_display_links = ["idUser"]
    list_filter = ["idUser"]

    class Meta:
        model = DetaRoles

admin.site.register(DetaRoles)

#Registro del modelo de Rates
class RatesModel(admin.ModelAdmin):
    list_display = ["idHabil"]
    list_display_links = ["idHabil"]
    list_filter = ["idHabil"]

    class Meta:
        model = Rates
        
admin.site.register(Rates)
