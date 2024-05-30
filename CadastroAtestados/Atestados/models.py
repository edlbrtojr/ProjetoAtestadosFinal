from django.db import models

class Atestado(models.Model):
    choices_ano = (('6', '6º ano'), ('7', '7º ano'), ('8', '8º ano'), ('9', '9º ano'))
    choices_turma = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                     ('E', 'E'), ('F', 'F'), ('APC', 'Aprender é o caminho'))
    
    nome_aluno = models.CharField(max_length=100)
    ano_aluno = models.CharField(max_length=50, choices=choices_ano)
    turma_aluno = models.CharField(max_length=50, choices=choices_turma)
    data_atestado = models.DateField()
    dias_afastamento = models.PositiveIntegerField()
    observacoes = models.TextField()
    arquivo = models.FileField(upload_to='atestados/uploads/%Y/%m/%d/')

    def __str__(self):
        return self.nome_aluno
