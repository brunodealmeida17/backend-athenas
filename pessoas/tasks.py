from .models import Pessoa
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

class PessoaTask:
    @staticmethod
    def criar_pessoa(dados):
        try:
            return Pessoa.objects.create(**dados)
        except Exception as e:
            print(f"Erro ao criar pessoa: {e}")
            return None

    @staticmethod
    def atualizar_pessoa(pessoa, dados):
        try:
            pessoa = get_object_or_404(Pessoa, id=pessoa)
            print(pessoa)
            print(dados)
            for key, value in dados.items():
                setattr(pessoa, key, value)
            pessoa.save()
            return pessoa
        except ObjectDoesNotExist:
            print("Pessoa não encontrada")
            return None
        except Exception as e:
            print(f"Erro ao atualizar pessoa: {e}")
            return None

    @staticmethod
    def excluir_pessoa(pessoa):
        try:
            print(pessoa)
            pessoa = get_object_or_404(Pessoa, id=pessoa)
            pessoa.delete()
        except ObjectDoesNotExist:
            print("Pessoa não encontrada")
        except Exception as e:
            print(f"Erro ao excluir pessoa: {e}")

    @staticmethod
    def listar_pessoas(cpf):
        try:
            if cpf:
                return Pessoa.objects.filter(cpf=cpf)
            return Pessoa.objects.all()
        except Exception as e:
            print(f"Erro ao listar pessoas: {e}")
            return None

