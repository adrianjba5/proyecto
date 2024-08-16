from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required


# @login_required
def inicio(request):
        return render(request, "apppreentrega/inicio.html")

def about(request):
        return render(request, 'apppreentrega/about.html')

def servicios(request):
        return render(request, 'apppreentrega/servicios.html')


class ClienteListView( LoginRequiredMixin,ListView):
        model = Client
        context_object_name = "clientes"
        template_name = "Apppreentrega/listar_cliente.html"
        
class ClienteCreateListView( LoginRequiredMixin,CreateView):
        model = Client
        template_name = "Apppreentrega/create_cliente.html"
        success_url = reverse_lazy("ListarClientes")
        fields = ["nombre", "apellido", "correo"]
        
class ClienteUpdateView( LoginRequiredMixin,UpdateView):
        model = Client
        template_name = "Apppreentrega/actualizar_cliente.html"
        fields = ["nombre", "apellido", "correo"]
        success_url = reverse_lazy("ListarClientes")
        
class ClienteDeleteView(LoginRequiredMixin,DeleteView):
        model = Client
        template_name = "Apppreentrega/borrar_cliente.html"
        success_url = reverse_lazy("ListarClientes")

# # Clases para clientes
# class CursoDeleteView(DeleteView):
#         model = Client
#         template_name = "Apppreentrega/borrar.html"
#         fields = ["nombre", "apellido", "correo"]
#         success_url = reverse_lazy("ListarC")



