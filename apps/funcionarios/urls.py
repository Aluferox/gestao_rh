from django.urls import path, include
from .views import (FuncionarioList,
                    FuncionarioEdit,
                    FuncionarioDelete,
                    FuncionarioNovo,
                    )


urlpatterns = [

    path('', FuncionarioList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),

]