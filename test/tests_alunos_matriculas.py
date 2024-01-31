from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse 
from escola.models import Matricula
from escola.models import Aluno
from escola.models import Curso
from rest_framework import status


class MatriculasTestCase(APITestCase):

  def setUp(self):
    # Simulando um usuário autentificado
    usuario_teste = User.objects.create_user(username='teste', password='teste')
    self.client.force_authenticate(user=usuario_teste)

    # Capturar a URL correspondente ao basename (Cursos-list)
    self.lista_url = reverse('Aluno_Matriculas', kwargs={'pk': 1})
    
    # Populando o banco de dados com exemplos
    self.aluno1 = Aluno.objects.create(nome='Nome teste 1',
                          rg='123456789',
                          cpf='12312312',
                          data_nascimento='2023-12-12',
                          celular= '123456789'
                          )
    
    self.curso1 = Curso.objects.create(codigo_curso="CTT1", descricao='Curso teste 1', nivel='M')

    self.matricula1 = Matricula.objects.create(aluno=self.aluno1, curso=self.curso1, periodo='A')
    self.matricula2 = Matricula.objects.create(aluno=self.aluno1, curso=self.curso1, periodo='A')
   
  def test_requisicao_get_para_listar_matriculas(self):
    """ Verifica se uma requisição do tipo GET está retornando um código 200 """
    resposta = self.client.get(self.lista_url)
    self.assertEquals(resposta.status_code, status.HTTP_200_OK)