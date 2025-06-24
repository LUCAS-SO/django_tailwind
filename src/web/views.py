from django.contrib import messages
from django.shortcuts import render


def inicio(request):
    return render(request, 'web/inicio.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        if nombre and email and mensaje:
            # En versión básica mostramos un mensaje, pero más adelante lo guardamos
            messages.success(request, '¡Gracias por tu mensaje! Te responderemos pronto.')
        else:
            messages.error(request, 'Por favor completá todos los campos.')

    return render(request, 'web/contacto.html')