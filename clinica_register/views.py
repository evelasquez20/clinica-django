from django.shortcuts import render
from .forms import MedicosForm

# Create your views here.

def clinica_list(request):
    return render(request, "clinica_register/clinica_list.html")

def clinica_form(request):
    form = MedicosForm()
    return render(request, "clinica_register/clinica_form.html", {'form':form})

def clinica_delete(request):
    return

