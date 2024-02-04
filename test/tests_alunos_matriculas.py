from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse 
from escola.models import Matricula
from escola.models import Aluno
from escola.models import Curso
from rest_framework import status

class MatriculasTestCase(APITestCase):
  def setUp(self):
    
    self.usuario_autenticado_para_teste()

    # Obtém a URL para a lista de matrículas de um aluno específico
    self.lista_url = reverse('Aluno_Matriculas', kwargs={'pk': 1})

    self.polular_banco_de_dados_para_teste()
   
  def test_requisicao_get_para_listar_matriculas(self):
    """ Testa se uma requisição GET retorna o status HTTP 200, indicando sucesso """
    resposta = self.client.get(self.lista_url)
    self.assertEquals(resposta.status_code, status.HTTP_200_OK)
    
  def usuario_autenticado_para_teste(self):
    """ Cria um usuário fictício para autenticação nos testes """
    usuario_teste = User.objects.create_user(username='teste', password='teste')
    self.client.force_authenticate(user=usuario_teste)

  def polular_banco_de_dados_para_teste(self):
    """ Cria registros de exemplo no banco de dados para testes """
    self.aluno1 = Aluno.objects.create(nome='Nome teste 1',
                            rg='123456789',
                            cpf='12312312',
                            data_nascimento='2023-12-12',
                            celular= '123456789'
                            )
      
    self.curso1 = Curso.objects.create(codigo_curso="CTT1", descricao='Curso teste 1', nivel='M')

    self.matricula1 = Matricula.objects.create(aluno=self.aluno1, curso=self.curso1, periodo='A')
    self.matricula2 = Matricula.objects.create(aluno=self.aluno1, curso=self.curso1, periodo='A')