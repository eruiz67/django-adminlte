# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import PersonModel, WorkerModel
from django.utils.translation import gettext_lazy as _

# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (_('Info personal'),
            {'fields': ('name','surname1','surname2','birthday_date','identification')}),
        (_('Info trabajador'), 
            {'fields': ('type',)}),
        (_('Datos del registro'),
            {'fields': ('active','create_date','create_uid','write_date','write_uid')}),
    )

    readonly_fields = ('create_date','create_uid','write_date','write_uid',)

admin.site.register(WorkerModel, WorkerAdmin)
