from django.urls import path
from clinica_register import views

urlpatterns = [
    path('', views.clinica_form, name= 'clinica_insert'),
    path('<int:id>/', views.clinica_form, name= 'clinica_update'),
    path('delete/<int:id>/', views.clinica_delete, name= 'clinica_delete'),
    path('listar/', views.clinica_list, name= 'clinica_list'),
]