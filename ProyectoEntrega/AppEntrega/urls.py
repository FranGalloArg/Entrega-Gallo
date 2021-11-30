from django.urls.conf import path
from .views import crear_ticket, crear_usuario, inicio, lista_tecnicos,lista_usuarios,lista_tickets,crear_tecnico


urlpatterns = [
    path('',inicio,name='inicio'),
    path('tecnicos/',lista_tecnicos,name='Tecnicos'),
    path('tecnicos/crear/',crear_tecnico,name='Crear_tecnico'),
    path('usuarios/',lista_usuarios,name='Usuarios'),    
    path('usuarios/crear/',crear_usuario,name='Crear_usuario'),
    path('tickets/',lista_tickets,name='Tickets'),   
    path('tickets/crear/',crear_ticket,name='Crear_ticket'),
]
