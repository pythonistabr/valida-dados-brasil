
"""
Author: Gustavo Leitao - 02-01-2022
github: pythonistabr
"""

from validate_docbr import CPF
from validate_docbr import CNPJ


class Documento:

    def __init__(self, numero):
        self.numero = numero
    
    @staticmethod
    def cria_novo(numero):
        numero_string = str(numero)
        
        if len(numero_string) == 11:
            return MyCpf(numero_string)
        
        if len(numero_string) == 14:
            return MyCnpj(numero_string)
        
        else:
            raise ValueError("O numero inserido é invalido")


class MyCpf:
    
    def __init__(self, numero):
        
        if self.valida(numero):
            self.numero = str(numero)
        else:
            raise ValueError("O CPF inserido é inválido")

    def valida(self, numero):
        self.numero = str(numero)
        
        if len(self.numero) == 11:
            validador = CPF()
            return validador.validate(self.numero)
        else:
            raise ValueError("O CPF inserido é inválido")
    
    def formata(self):
        formatador = CPF()
        numero_formatado = formatador.mask(self.numero)
        return numero_formatado
    
    
    def __str__(self):
        return self.formata()




class MyCnpj:

    def __init__(self, numero):
        
        if self.valida(numero):
            self.numero = str(numero)
        else:
            raise ValueError("O CNPJ inserido é invalido!")

    def valida(self, numero):
        self.numero = str(numero)
        
        if len(self.numero) == 14:
            validador = CNPJ()
            return validador.validate(self.numero)
        else:
            raise ValueError("O CNPJ inserido é inválido!")

    
    def formata(self):
        formatador = CNPJ()
        numero_formatado = formatador.mask(self.numero)
        return numero_formatado

    
    def __str__(self):
        return self.formata()

def main():
    
    my_cpf = MyCpf("45110173010")
    print(my_cpf)
    print("---------------------")
    my_cnpj = MyCnpj("95119791000180")
    print(my_cnpj)

if __name__ == "__main__":
    main()