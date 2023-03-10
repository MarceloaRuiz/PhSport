from django.shortcuts import render, get_object_or_404
from .models import Paciente

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista_pacientes.html', {'pacientes': pacientes})

def detalle_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'pacientes/detalle_paciente.html', {'paciente': paciente})

