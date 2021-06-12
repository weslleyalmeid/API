from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.


class Evento(models.Model):
    # Campo varchar limitado
    titulo = models.CharField(max_length=100)
    # Campo texto ilimitado
    descricao = models.TextField(blank=True, null=True)
    # verbosidade customiza o nome que aparece no front
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    # Inserete automaticamente a data atual
    data_criacao = models.DateTimeField(auto_now=True)

    # Se o usuario for deletado, exlcluir todos os eventos e dependentes dele vai ser excluido
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    local = models.CharField(max_length=200, blank=True, null=True)

    # nome da tabela no banco de dados
    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y - %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        return False

    def get_evento_agora(self):
        import ipdb

        # ipdb.set_trace()
        if self.data_evento.date() == datetime.now().date():

            hora_evento = self.data_evento.hour
            minuto_evento = self.data_evento.minute
            hora_atual = datetime.now().hour
            minuto_atual = datetime.now().minute
            # ipdb.set_trace()
            hora = timedelta(hours=hora_evento, minutes=minuto_evento) - timedelta(hours=hora_atual, minutes=minuto_atual)

            # ipdb.set_trace()

            if hora.seconds < 3600:
                return True
        
        return False