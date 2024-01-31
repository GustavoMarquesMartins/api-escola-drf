from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from escola.models import Aluno
from django.urls import reverse 
from rest_framework import status


class AlunosTestCase(APITestCase):

  def setUp(self):
      # Simulando um usuário autentificado
      usuario_teste = User.objects.create_user(username='teste', password='teste')
      self.client.force_authenticate(user=usuario_teste)

      # Capturar a URL correspondente ao basename (Alunos-list)
      self.lista_url = reverse('Alunos-list')

      # Populando o banco de dados com exemplos
      self.aluno1 = Aluno.objects.create(nome='Nome teste 1',
                          rg='123456789',
                          cpf='12312312',
                          data_nascimento='2023-12-12',
                          celular= '123456789'
                          )
      
      self.aluno2 = Aluno.objects.create(nome='Nome teste 3',
                          rg='12345678',
                          cpf='12312311',
                          data_nascimento='2023-12-12',
                          celular= '123456781'
                          )

  def test_requisicao_get_para_listar_alunos(self):
    """ Verifica se uma requisição do tipo GET está retornando um código 200 """
    response = self.client.get(self.lista_url)
    self.assertEquals(response.status_code, status.HTTP_200_OK)

  def test_requisicao_post_para_criar_aluno(self):
    """ Verifica se uma requisição do tipo POST está retornando um código 201 """
    data = {
        "nome" : 'Nome teste 1',
        "rg":'123456789',
        "cpf":'12312312',
        "data_nascimento":'2023-12-12',
        "celular":'123456781'
        }
    
    response = self.client.post(self.lista_url, data=data) 
    self.assertEquals(response.status_code, status.HTTP_201_CREATED)
  
  def test_requisicao_delete_para_excluir_aluno(self):
    """ Verifica se uma requisição do tipo DELETE está retornando um código 204 """
    response = self.client.delete(self.lista_url + '1/')
    self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
  
  def test_requisicao_put_para_atualizar_aluno(self):
    """ Verifica se uma requisição do tipo PUT está retornando um código 200 """
    data =  {'id': 1,
              'nome': 'Nome teste 1',
              'rg': '87654321',
              'cpf': '12312311',
              'data_nascimento': '2023-12-12'
              }
        
    response = self.client.put(self.lista_url + '1/', data=data)
    self.assertEquals(response.status_code, status.HTTP_200_OK)


     
     

