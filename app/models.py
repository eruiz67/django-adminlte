#from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.fields.related import ManyToManyField
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.core.validators import MinValueValidator, RegexValidator
from django.db.models import Q

class BaseModel(models.Model):
    """
    Modelo abstracto que registra los cambios realizados a las tablas de la base de datos. Tiene relaciones con
    :model:`auth.User`.
    """

    create_date = models.DateTimeField('fecha creación', editable=False, auto_now_add=True)
    create_uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   related_name='+', verbose_name=_('creado por'), editable=False, null=True, blank=True)
    write_date = models.DateTimeField(verbose_name=_('última modificación'), null=True, blank=True,
                                      editable=False, auto_now=True)
    write_uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                       null=True, blank=True, related_name='+',
                                       verbose_name='modificado por', editable=False)
    active = models.BooleanField(verbose_name=_('Activo?'), default=True)

    class Meta:
        abstract = True
        verbose_name = _("Registro")
        verbose_name_plural = _("Registros")

class PersonModel(BaseModel):

    name = models.CharField(verbose_name=_("Nombre "), max_length=50,  blank=False, null=False)
    surname1 = models.CharField(verbose_name=_("Primer apellido"), max_length=50,  blank=False, null=False)
    surname2 = models.CharField(verbose_name=_("Segundo apellido"), max_length=50,  blank=False, null=False)

    identification = models.CharField(verbose_name=_("Carnet"), max_length=11, unique=True, blank=False, null=False,validators=[RegexValidator(regex=r"(^[\d]{11}$)", message=_("El carnet debe contener 11 dígitos"))])
    
    birthday_date =  models.DateField(verbose_name=_("Fecha de nacimiento"),  blank=False, null=False)

    identification_image_front = models.FileField(verbose_name=_("Foto carnet frontal"), upload_to="app_person_identification_image_front",
                                                null=True, blank=True)

    def limit_categories_choices():
        #return {'type': 'worker'}
        return (Q(type='worker')|Q(type='person'))

    categories = models.ManyToManyField("CategoryModel",verbose_name=_("Categorías"), 
                                        limit_choices_to=limit_categories_choices, null=True, blank=True)
    
    
    
    def __str__(self):
        return "{} {} {}".format(self.name, self.surname1, self.surname2)
    
    @property
    def get_full_name(self):
        return "{} {} {}".format(self.name, self.surname1, self.surname2)

    class Meta:
        db_table = 'app_person'
        managed = True
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')

class StudentModel(PersonModel):

    YEAR_CHOICES = (
        ('1', _('Primero')),
        ('2', _('Segundo')),
        ('3', _('Tercero')),
        ('4', _('Cuarto')),
        ('5', _('Quinto')),
        ('post', _('Posgrado')),
        
    )
    year =  models.CharField(verbose_name=_("Año"), max_length=50, choices=YEAR_CHOICES)
    
    class Meta:
        db_table = 'app_student'
        managed = True
        verbose_name = _('Estudiante')
        verbose_name_plural = _('Estudiantes')


class WorkerModel(PersonModel):

    WORKER_TYPE_CHOICES = (
        ('fixed', _('Fijo')),
        ('contract', _('Contrato')),    
    )
    type =  models.CharField(verbose_name=_("Tipo trabajador"), max_length=50, choices=WORKER_TYPE_CHOICES )
    area = models.ForeignKey("AreaModel", verbose_name=_("Area"), 
                        related_name="workers", on_delete=models.CASCADE,
                         blank=True, null=True)
    department = models.ForeignKey("DepartmentModel", verbose_name=_("Departamento"), 
                        related_name="workers", on_delete=models.CASCADE,
                         blank=True, null=True)
    is_social_service = models.BooleanField(_('Servicio social'), default=False)    

    class Meta:
        db_table = 'app_worker'
        managed = True
        verbose_name = _('Trabajador')
        verbose_name_plural = _('Trabajadores')

class AreaModel(BaseModel):

    name = models.CharField(verbose_name=_('Nombre'),max_length=50,  unique=True, blank=False, null=False)
    description = models.TextField(verbose_name=_('Descripción'),max_length=500, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_area'
        managed = True
        verbose_name = _('Area')
        verbose_name_plural = _('Areas')


class DepartmentModel(BaseModel):

    name = models.CharField(verbose_name=_('Nombre'),max_length=50,  unique=True, blank=False, null=False)
    description = models.TextField(verbose_name=_('Descripción'),max_length=500, blank=True, null=True)
    area = models.ForeignKey("AreaModel", verbose_name=_("Área"), 
                            related_name="departments", on_delete=models.CASCADE)


    def __str__(self):
        return "{} - {}".format(self.area.name,self.name)

    class Meta:
        db_table = 'app_department'
        managed = True
        verbose_name = _('Departamento')
        verbose_name_plural = _('Departamentos')



class CategoryModel(BaseModel):

    CATEGORY_TYPE_CHOICES = (
        ('person', _('Persona')),
        ('worker', _('Trabajador')), 
        ('student', _('Estudiante')),      
    )

    name = models.CharField(verbose_name=_('Nombre'),max_length=50,  unique=True, blank=False, null=False)
    description = models.TextField(verbose_name=_('Descripción'),max_length=500, blank=True, null=True)
    type =  models.CharField(verbose_name=_("Tipo Categoría"), max_length=50, 
                                            choices=CATEGORY_TYPE_CHOICES, blank=True, null=True )


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_category'
        managed = True
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'