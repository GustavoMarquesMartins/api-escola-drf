from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse 
from rest_framework import status
from django.contrib.auth.models import User
import json
from rest_framework.test import APIClient


class CursosTestCase(APITestCase):

    def setUp(self):
        # Simulando um usuário autentificado
        usuario_teste = User.objects.create_user(username='teste', password='teste')
        self.client.force_authenticate(user=usuario_teste)

        # Capturar a URL correspondente ao basename (Cursos-list)
        self.lista_url = reverse('Cursos-list')

        # Populando o banco de dados com exemplos
        self.curso1 = Curso.objects.create(codigo_curso="CTT1", descricao='Curso teste 1', nivel='B')
        self.curso2 = Curso.objects.create(codigo_curso="CTT2", descricao='Curso teste 2', nivel='A')

    def test_requisicao_get_para_listar_cursos(self):
        """ Verifica se uma requisição do tipo GET está retornando um código 200 """
        response = self.client.get(self.lista_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """ Verifica se uma requisição do tipo POST está retornando um código 201 """
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'B'
        }
        response = self.client.post(self.lista_url, data=data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_delete_para_falhar_ao_tentar_excluir_curso(self):
        """ Verifica se a requisição do tipo DELETE está retornando um código 405 """
        response = self.client.delete(self.lista_url + '1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_put_para_atualizar_curso(self):
        """ Verifica se uma requisição do tipo PUT está retornando um código 200 """
        data = {
            'codigo_curso' : 'CTT4',
            'descricao' : 'Curso teste 4',
            'nivel' : 'B'
        }
        response = self.client.put(self.lista_url + '1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK )

        