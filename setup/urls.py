from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

# Registro das ViewSets no roteador para criar automaticamente as URLs
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    # URL para o painel de administração do Django, que é sobrescrita para evitar requisições indesejadas
    path('painel-de-controle/', admin.site.urls),
    
    # URL para integrar o 'admin_honeypot', que é uma ferramenta de segurança para prevenir ataques de força bruta
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    
    # URL para incluir as rotas geradas automaticamente pelo roteador
    path('', include(router.urls)),
    
    # URL personalizada para listar todas as matrículas de um aluno específico
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view(), name='Aluno_Matriculas'),
    
    # URL personalizada para listar todos os alunos matriculados em um curso específico
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view(), name='Curso_Matriculas')
    
    # Adição de suporte para servir arquivos de mídia estáticos durante o desenvolvimento
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


