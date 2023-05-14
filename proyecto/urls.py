from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    #cuando el usuario entre, se muestra el inicio
    path('nosotros', views.nosotros, name='nosotros'),
    path('articulos', views.articulos, name='articulos'),
    path('articulos/crear', views.crear, name='crear'),
    path('articulos/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('articulos/editar/<int:id>', views.editar, name='editar'),
]