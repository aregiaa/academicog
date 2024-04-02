from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
class Ocupacoe(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Instituicoe(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.cidade}, {self.nome}'

class AreaDosSabere(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'


class Pessoa(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacoe, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.ocupacao}, {self.nome}, {self.email}'
    

class Curso(models.Model):
    instituicao = models.ForeignKey(Instituicoe, on_delete=models.CASCADE)
    area_saber = models.ForeignKey(AreaDosSabere, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()

    def __str__(self):
        return f'{self.instituicao}, {self.area_saber}, {self.nome}, {self.carga_horaria_total}, {self.duracao_meses}'

class PeriodoCurso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'
    
class Disciplina(models.Model):
    area_saber = models.ForeignKey(AreaDosSabere, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.area_saber}, {self.nome}'

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicoe, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f'{self.instituicao}, {self.curso}, {self.pessoa}, {self.data_inicio}, {self.data_previsao_termino}'
    
class Avaliacoe(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.disciplina}, {self.curso}, {self.descricao}'
    
class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

    def __str__(self):
        return f'{self.pessoa}, {self.disciplina}, {self.curso}, {self.numero_faltas}'
    
class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.nome}, {self.turno}'
    
class Ocorrencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=300)
    data = models.DateField()

    def __str__(self):
        return f'{self.curso}, {self.disciplina}, {self.pessoa}, {self.descricao}, {self.data}'

class DisciplinaCurso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(PeriodoCurso, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return f'{self.disciplina}, {self.curso}, {self.periodo}, {self.carga_horaria}'
    
class TipoAvaliação(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'