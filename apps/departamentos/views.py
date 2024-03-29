from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento

class DepartamentoList(ListView):
    model = Departamento
    allow_empty = True

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list-departamentos')

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)

class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list-departamentos')


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list-departamentos')
