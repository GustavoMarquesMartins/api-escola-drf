from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse 
from rest_framework import status
from django.contrib.auth.models import User


class CursosTestCase(APITestCase):

    def setUp(self):
        self.usuario_autenticado_para_teste()

        # Obtém a URL para a lista de cursos
        self.lista_url = reverse('Cursos-list')

        self.polular_banco_de_dados_para_teste()

    def test_requisicao_get_para_listar_cursos(self):
        """ Testa se uma requisição GET retorna o status HTTP 200, indicando sucesso """
        response = self.client.get(self.lista_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """ Testa se uma requisição POST retorna o status HTTP 201, indicando que um recurso foi criado """
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'B'
        }

        response = self.client.post(self.lista_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_para_falhar_ao_tentar_excluir_curso(self):
        """ Testa se uma requisição DELETE retorna o status HTTP 405, indicando que o método não é permitido """
        response = self.client.delete(self.lista_url + '1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_put_para_atualizar_curso(self):
        """ Testa se uma requisição PUT retorna o status HTTP 200, indicando que um recurso foi atualizado """
        data = {
            'codigo_curso' : 'CTT4',
            'descricao' : 'Curso teste 4',
            'nivel' : 'B'
        }
        
        response = self.client.put(self.lista_url + '1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK )
    
    def usuario_autenticado_para_teste(self):
        """ Cria um usuário fictício para autenticação nos testes """
        usuario_teste = User.objects.create_user(username='teste', password='teste')
        self.client.force_authenticate(user=usuario_teste)

    def polular_banco_de_dados_para_teste(self):
        """ Cria registros de exemplo no banco de dados para testes """
        self.curso1 = Curso.objects.create(codigo_curso="CTT1", descricao='Curso teste 1', nivel='B')
        self.curso2 = Curso.objects.create(codigo_curso="CTT2", descricao='Curso teste 2', nivel='A')
