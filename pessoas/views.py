from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pessoa
from .serializers import PessoaSerializer
from .services import PessoaService
from .tasks import PessoaTask
from rest_framework.exceptions import NotFound
from rest_framework import status


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer   

    @action(detail=True, methods=['get'])
    def calcular_peso_ideal(self, request, pk=None):
        try:
            pessoa = Pessoa.objects.get(pk=pk)
            peso_ideal = PessoaService.calcular_peso_ideal(pessoa)

            return Response({"peso_ideal": round(peso_ideal, 2)}, status=status.HTTP_200_OK)
        
        except Pessoa.DoesNotExist:
            return Response({"erro": "Pessoa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'], url_path="buscar_por_cpf")
    def buscar_por_cpf(self, request):
        cpf = request.query_params.get('cpf', None)

        if not cpf:
            return Response({"error": "CPF é obrigatório"}, status=400)

        pessoas = PessoaTask.listar_pessoas(cpf)
        if not pessoas.exists():
            raise NotFound("CPF não encontrado.")

        serializer = self.get_serializer(pessoas, many=True)
        return Response(serializer.data)