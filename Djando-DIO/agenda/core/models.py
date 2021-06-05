from django.db import models
from django.contrib.auth.models import User

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

    # nome da tabela no banco de dados
    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y - %H:%M Hrs')