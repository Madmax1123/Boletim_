from django.shortcuts import render
from .models import Boletim
def home(request):
    notas = {}
    notas['boletims'] = Boletim.objects.all()
    nota1 = Boletim.objects.get(pk=1)
    res = nota1
    res.save()
    notas['calculo'] = res
    return render(request, 'boletim.html', notas)