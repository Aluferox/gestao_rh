from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.urls import reverse_lazy

# Create your views here.
class FuncionariosList(ListView):
    model = Funcionario
    allow_empty = True

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamento']
    template_name_suffix = '_update_form'


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionario')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')
        if len(username) ==1:
            username = username[0]
        elif len(username) >1:
            username = username[0] + username[1]


        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(
            username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)
        
