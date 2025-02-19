from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from pessoas.models import Pessoa

class PessoaAPITestCase(TestCase):
    """ Testes para a API de Pessoas """

    def setUp(self):
        """ Configuração inicial para cada teste """
        Pessoa.objects.all().delete() # Limpa a tabela de pessoas
        self.client = APIClient()
        self.pessoa_data = {
            "nome": "João da silva",
            "data_nasc": "1990-05-20",
            "cpf": "12345678978",
            "sexo": "M",
            "altura": 1.75,
            "peso": 80.0
        }
        self.pessoa = Pessoa.objects.create(**self.pessoa_data)
        self.url = reverse("pessoa-list")  

    def test_criar_pessoa(self):
        """ Teste para criação de uma pessoa """
        nova_pessoa_data = {
            "nome": "Maria Souza",
            "data_nasc": "1995-08-15",
            "cpf": "98765432100",  
            "sexo": "F",
            "altura": 1.65,
            "peso": 60.0
        }
        response = self.client.post(self.url, nova_pessoa_data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_pessoas(self):
        """ Teste para listar todas as pessoas """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_atualizar_pessoa(self):
        """ Teste para atualizar uma pessoa """
        url_detalhe = reverse("pessoa-detail", kwargs={"pk": self.pessoa.id})  
        novo_dado = {"nome": "João Pedro Silva"}
        response = self.client.patch(url_detalhe, novo_dado, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pessoa.refresh_from_db()
        self.assertEqual(self.pessoa.nome, "João Pedro Silva")

    def test_excluir_pessoa(self):
        """ Teste para deletar uma pessoa """
        url_detalhe = reverse("pessoa-detail", kwargs={"pk": self.pessoa.id})  
        response = self.client.delete(url_detalhe)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pessoa.objects.count(), 0)

    def test_calculo_peso_ideal(self):
        """ Teste para verificar o cálculo do peso ideal """
        url_peso_ideal = reverse("pessoa-calcular-peso-ideal", kwargs={"pk": self.pessoa.id})
        response = self.client.get(url_peso_ideal)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificando o cálculo correto do peso ideal para homens
        peso_ideal_esperado = (72.7 * self.pessoa.altura) - 58
        self.assertAlmostEqual(response.json()["peso_ideal"], peso_ideal_esperado, places=1)
