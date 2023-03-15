from django.urls import path
from AppConsultorio.views import *
from pacientes.views import lista_pacientes, detalle_paciente

urlpatterns = [
    path('index/', index),
    path('', lista_pacientes, name='lista_pacientes'),
    path('paciente/<int:pk>/', detalle_paciente, name='detalle_paciente'),
]