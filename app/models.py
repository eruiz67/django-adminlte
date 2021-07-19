#from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

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

    identification = models.CharField(verbose_name=_("Carnet"), max_length=11,  blank=False, null=False)
    
    birthday_date =  models.DateField(verbose_name=_("Fecha de nacimiento"),  blank=False, null=False)


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
    

    class Meta:
        db_table = 'app_worker'
        managed = True
        verbose_name = _('Trabajador')
        verbose_name_plural = _('Trabajadores')
