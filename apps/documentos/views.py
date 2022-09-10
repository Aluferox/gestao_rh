from .models import Documento
from django.views.generic import CreateView
from django.urls import reverse_lazy

class DocumentCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['pk']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_valid(form)