from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import path
from apppreentrega import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("listar_cliente/", views.ClienteListView.as_view(), name="ListarClientes"),
    path("crear_cliente/", views.ClienteCreateListView.as_view(), name="CrearClientes"),
    path("actualizar/<pk>/", views.ClienteUpdateView.as_view(), name="ActualizarClientes"),
    path("borrar_cliente/<pk>/", views.ClienteDeleteView.as_view(), name="BorrarClientes"),
    path('about/', views.about, name='about'),
    path('servicios/', views.servicios, name='servicios'),
    
    
    

    
]
