"""
busca e validação de CEP 
by: @pythonistabr
"""
import requests

class CepBrasil:
    
    def __init__(self, cep):
        self.cep = str(cep)
        
        if self.valida_cep():
            self.cep = str(cep)
        
        else:
            raise ValueError("CEP inválido.")


    def valida_cep(self):
        
        if len(self.cep) == 8:
            return True
        else:
            return False


    def formata_cep(self):
        return "{}-{}".format(self.cep[0:5], self.cep[5::])
    

    def __str__(self):
        return self.formata_cep()

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        response = requests.get(url)
        dados = response.json()
        return (dados['bairro'],
        dados['localidade'],
        dados['uf'])
        


def main():
    #mycep = CepBr(12345678)
    #print(mycep)

    cep = "68890970"
    objeto_cep = CepBrasil(cep)

    #r = requests.get("https://viacep.com.br/ws/01001000/json/")
    #print(r.text)

    bairro, cidade, uf = objeto_cep.acessa_via_cep()
    print(f"Bairro: {bairro}, cidade: {cidade}, Estado: {uf}")

    
if __name__ == "__main__":
    main()
