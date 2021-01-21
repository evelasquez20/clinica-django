from django.shortcuts import render, redirect
from .forms import MedicosForm
from .models import Medicos

# Create your views here.

def clinica_list(request):
    context = {'clinica_list': Medicos.objects.all()}
    return render(request, "clinica_register/clinica_list.html", context)

def clinica_form(request, id= 0):
    if request.method == "GET":
        if id == 0:
            form = MedicosForm()
        else:
            medico = Medicos.objects.get(pk=id)
            form = MedicosForm(instance=medico)
        return render(request, "clinica_register/clinica_form.html", {'form':form})
    else:
        if id == 0:
            form = MedicosForm(request.POST)
        else:
            medico = Medicos.objects.get(pk=id)
            form = MedicosForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
        return redirect('/clinica/listar')

def clinica_delete(request, id):
    medico = Medicos.objects.get(pk=id)
    medico.delete()
    return redirect('/clinica/listar')

