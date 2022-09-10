from django.urls import path
from .views import DepartamentoList, DepartamentoCreate, DepartamentoEdit, DepartamentoDelete

urlpatterns = [
    path('list/', DepartamentoList.as_view(), name='list-departamentos'),
    path('novo/', DepartamentoCreate.as_view(), name='create-departamento'),
    path('editar/<int:pk>/', DepartamentoEdit.as_view(), name='update-departamento'),
    path('deletar/<int:pk>/', DepartamentoDelete.as_view(), name='delete-departamento'),
]