from django.shortcuts import render, redirect
from .forms import MedicosForm

# Create your views here.

def clinica_list(request):
    return render(request, "clinica_register/clinica_list.html")

def clinica_form(request):
    if request.method == "GET":
        form = MedicosForm()
        return render(request, "clinica_register/clinica_form.html", {'form':form})
    else:
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/clinica/listar')

def clinica_delete(request):
    return

