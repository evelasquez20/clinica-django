from django.urls import path
from . import views

urlpatterns = [
    path('', views.clinica_form),
    path('listar/', views.clinica_list),
]