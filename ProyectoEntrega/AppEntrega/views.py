from io import StringIO
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import TecnicosFormulario, TicketFormulario, UsuariosFormulario
from .models import Tecnico, Ticket, Usuario

# Create your views here.

def inicio (request):
    
    return render (request,'AppEntrega/inicio.html',{})

def lista_tecnicos (request):
    tecnicos = None
    error = None
    if request.method == 'GET':
        edificio = request.GET.get('edificio','')
        if edificio == '':
            tecnicos = Tecnico.objects.all()
        else:
            tecnicos = Tecnico.objects.filter(edificio=edificio)
    return render (request, 'AppEntrega/lista_tecnicos.html ',{'tecnicos':tecnicos, 'error':error} )

def crear_tecnico (request):
    if request.method == 'POST':
        formulario = TecnicosFormulario(request.POST)
        if  formulario.is_valid():
            datos = formulario.cleaned_data
            tecnico = Tecnico(nombre=datos['nombre'],apellido=datos['apellido'],email=datos['email'],edificio=datos['edificio'])
            tecnico.save()
            # return render (request,'AppEntrega/lista_tecnicos.html',{'tecnicos':None,'error':None})
            return redirect ('Tecnicos')
    
    formulario = TecnicosFormulario()
    return render(request,'AppEntrega/formulario_tecnico.html',{'formulario':formulario})


def lista_usuarios (request):
    usuarios = None
    error = None
    if request.method == 'GET':
        legajo = request.GET.get('legajo','')
        if legajo == '':
            usuarios = Usuario.objects.all()
        else:
            usuarios = Usuario.objects.filter(legajo=legajo)
    
    return render (request,'AppEntrega/lista_usuarios.html',{'usuarios':usuarios,'error':error})

def crear_usuario (request):
    if request.method == 'POST':
        formulario = UsuariosFormulario(request.POST)
        if  formulario.is_valid():
            datos = formulario.cleaned_data
            usuario = Usuario(nombre=datos['nombre'],apellido=datos['apellido'],email=datos['email'],legajo=datos['legajo'])
            usuario.save()
            # return render (request,'AppEntrega/lista_tecnicos.html',{'tecnicos':None,'error':None})
            return redirect ('Usuarios')
    
    formulario = UsuariosFormulario()
    return render(request,'AppEntrega/formulario_usuario.html',{'formulario':formulario})

def lista_tickets (request):
    tickets = None
    error = None
    if request.method == 'GET':
        numero = request.GET.get('numero','')
        if numero == '':
            tickets = Ticket.objects.all()
        else:
            try:
                numero = int(numero)
                tickets = Ticket.objects.filter(numero=numero)
            except:
                error = 'Debes ingresar numero entero'
    
    return render (request,'AppEntrega/lista_tickets.html',{'tickets':tickets,'error':error})

def crear_ticket (request):
    if request.method == 'POST':
        formulario = TicketFormulario(request.POST)
        if  formulario.is_valid():
            datos = formulario.cleaned_data
            ticket = Ticket(numero=datos['numero'],estado=datos['estado'])
            ticket.save()
            return redirect ('Tickets')
    
    formulario = TicketFormulario()
    return render(request,'AppEntrega/formulario_ticket.html',{'formulario':formulario})