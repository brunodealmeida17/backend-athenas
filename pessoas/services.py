class PessoaService:
    @staticmethod
    def calcular_peso_ideal(pessoa):
        if pessoa.sexo == 'M':
            return (72.7 * pessoa.altura) - 58
        else:
            return (62.1 * pessoa.altura) - 44.7