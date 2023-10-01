from django.shortcuts import render
from .models import Estudiante

# Create your views here.
def index(request):
    return render(request, 'estudiantes/index.html', {
        'estudiantes': Estudiante.objects.all()
    })