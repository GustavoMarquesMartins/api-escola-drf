from django.contrib import admin
from django.urls import path,include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static 

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view(), name='Aluno_Matriculas'), # retornar todas as matriculas realizadas por um aluno
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view(), name='Curso_Matriculas')  # retornar todas as matriculas feita para um curso
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
