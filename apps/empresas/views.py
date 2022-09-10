from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from .models import Empresa
from django.urls import reverse_lazy

class EmpresaCreate(CreateView):
    model = Empresa
    #success_url = reverse_lazy('create_empresa')
    fields = ['nome']

    def form_valid(self, form):
        empresa = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = empresa
        funcionario.save()
        return HttpResponse('ok')


class empresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']