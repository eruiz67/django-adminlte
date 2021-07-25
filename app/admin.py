# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import (PersonModel, WorkerModel, AreaModel,
DepartmentModel, CategoryModel)
from django.utils.translation import gettext_lazy as _

# Register your models here.

class WorkerAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (_('Info personal'),
            {'fields': ('name','surname1','surname2','birthday_date','identification','identification_image_front')}),
        (_('Info trabajador'), 
            {'fields': ('type','area','department','is_social_service')}),
        (_('Datos del registro'),
            {'fields': ('active','create_date','create_uid','write_date','write_uid')}),
    )

    readonly_fields = ('create_date','create_uid','write_date','write_uid',)

admin.site.register(WorkerModel, WorkerAdmin)

class AreaAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (_('Info general'),
            {'fields': ('name','description')}),
        (_('Datos del registro'),
            {'fields': ('active','create_date','create_uid','write_date','write_uid')}),
    )

    readonly_fields = ('create_date','create_uid','write_date','write_uid',)

admin.site.register(AreaModel, AreaAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (_('Info general'),
            {'fields': ('name','description','area')}),
        (_('Datos del registro'),
            {'fields': ('active','create_date','create_uid','write_date','write_uid')}),
    )

    readonly_fields = ('create_date','create_uid','write_date','write_uid',)

admin.site.register(DepartmentModel, DepartmentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    
    fieldsets = (
        (_('Info general'),
            {'fields': ('name','description','type')}),
        (_('Datos del registro'),
            {'fields': ('active','create_date','create_uid','write_date','write_uid')}),
    )

    readonly_fields = ('create_date','create_uid','write_date','write_uid',)

admin.site.register(CategoryModel, CategoryAdmin)
