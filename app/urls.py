# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app.views import views
from app.views import worker_views

app_name="app"

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('trabajador/lista/', worker_views.WorkerListView.as_view(), name='worker_list'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
