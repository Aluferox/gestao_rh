from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
                                  ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView,
                                  )
from .models import Funcionario


class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        #pegando empresa logada
        empresa_logada = self.request.user.funcionario.empresa
        #fintrando pelo nome da empresa logada no banco de dados.
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        #commit = não grava objeto no bancos de dados, armazena em memória para modificações.
        funcinario = form.save(commit=False)

        #separando nome do funcionário para criar um username
        username = funcinario.nome.split(' ')

        ##definido a empresa do funcionário
        funcinario.empresa = self.request.user.funcionario.empresa

        #crianco um usuário para o funcionário (username)
        funcinario.user = User.objects.create(username=''.join(username))

        return super(FuncionarioNovo, self).form_valid(form)





