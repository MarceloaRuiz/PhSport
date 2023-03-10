from django.shortcuts import render
from django.template import context


# Create your views here.
def index(request):
    return render(request, "PhSport/base.html")