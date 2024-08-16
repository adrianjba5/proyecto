from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import login_request, register, editar_perfil
from users import views



urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='apppreentrega/inicio.html'), name="Logout"),
    path('editar_perfil/', views.editar_perfil, name="EditarPerfil"),
    path('cambiar_contrasenia/', views.CambiarContreasenia.as_view(), name="CambiarContraseña")
    ]