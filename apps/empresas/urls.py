from django.urls import path
from .views import EmpresaCreate,empresaEdit


urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', empresaEdit.as_view(), name='edit_empresa'),
]