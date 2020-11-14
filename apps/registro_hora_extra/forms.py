from django.forms import ModelForm
from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraForm(ModelForm):

    # método de inicialização do formulário (variável user foi injetada por mim)
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)

        # Sobrescrevendo o conteúdo do field funcionário
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa=user.funcionario.empresa)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']