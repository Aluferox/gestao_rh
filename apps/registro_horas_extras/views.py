from django.urls import reverse_lazy
from .models import RegistroHoraExtra
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .forms import RegistroHoraExtraForm

class HoraExtraList(ListView):
    model = RegistroHoraExtra
    allow_empty = True

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    template_name_suffix = '_update_form'
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_funcionario')


class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    # success_url = reverse_lazy('list_hora_extra')
    template_name_suffix = '_create_form'
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs