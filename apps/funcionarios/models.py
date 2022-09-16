from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.urls import reverse_lazy
from django.db.models import Avg, Count, Min, Sum

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('list_funcionario')

    @property
    def total_horas_extras(self):
        total = self.registrohoraextra_set.all().aggregate(Sum('horas'))['horas__sum']
        return total

    def __str__(self):
        return self.nome
