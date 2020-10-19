from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = [
        'nome',
    ]


    #Sobreescrevendo o metódo for_valid
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        a = funcionario.user
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('OK')
