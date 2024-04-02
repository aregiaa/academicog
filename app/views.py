from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic.base import TemplateView


from .models import *
from django.views import View

from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione aqui qualquer contexto adicional que você deseja passar para o template
        return context


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacoe.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})
    
class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicoe.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})
    
class AreaDosSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaDosSabere.objects.all()
        return render(request, 'area_Saber.html', {'areas': areas})
    
class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})
    
class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})
    
class PeriodoCursoView(View):
    def get(self, request, *args, **kwargs):
        periodos = PeriodoCurso.objects.all()
        return render(request, 'periodo_curso.html', {'periodos': periodos})
    
class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})
    
class MatriculaView(View):  
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacoe.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})
    
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})
    
class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})
    
class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})
    
class DisciplinaCursoView(View):
    def get(self, request, *args, **kwargs):
        disciplinas_cursos = DisciplinaCurso.objects.all()
        return render(request, 'disciplina_curso.html', {'disciplinas_cursos': disciplinas_cursos})
    
class TipoAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipos = TipoAvaliação.objects.all()
        return render(request, 'tipo_avaliacao.html', {'tipos': tipos})
