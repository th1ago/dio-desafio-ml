'''
bloco de codigo
'''

import re


def calcular_tot(numero):
    return sum(numero)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

#print(calcular_tot([10, 20])) #30
#print(retorna_antecessor_e_sucessor(10)) #(9,11)

# passagem de argumentos
def salvar_carro(marca, modelo, ano, placa):
    print(marca, modelo, ano, placa)    

salvar_carro("Fiat", "Doblo", 2000, "123ABC")
salvar_carro(marca="Fiat", modelo="Doblo", ano=2000, placa="123ABC")
# passando um dict
salvar_carro(**{"marca":"Fiat", "modelo":"Doblo", "ano":2000, "placa":"123ABC"})
