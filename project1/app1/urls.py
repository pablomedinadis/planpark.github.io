from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('centrosocio/', views.centrosocio),
    path('database/', views.database),
    path('registro/', views.registro),
    path('registro/add/', views.add),
    #path('add/', views.add),
    path('modificar/<int:id>', views.modificar,name='modificar'),
    path('database/editar/<int:id>', views.editar),
    path('database/eliminar/<int:id>', views.eliminar),
]
