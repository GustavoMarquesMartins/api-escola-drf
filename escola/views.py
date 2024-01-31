from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer, AlunoSerializerV2
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

    
class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    http_method_names = ['post','get','put','delete']

    def create(self, request):
        return custom_create(self, request, self.serializer_class) 
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return self.serializer_class
    

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    
    def create(self, request):
        return custom_create(self, request, self.serializer_class) 
    

class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    def create(self, request):
        return custom_create(self, request, self.serializer_class) 
    
    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(MatriculaViewSet, self).dispatch(*args, **kwargs)
    
class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer


def custom_create(self, request, serializer_class):
    """ Função 'create' personalizada para retornar url com campo Location  """
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        id = str(serializer.data['id'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers= {'Location': request.build_absolute_uri() + id})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
