'''
bloco de codigo
'''
def calcular_tot(numero):
    return sum(numero)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_tot([10, 20])) #30
print(retorna_antecessor_e_sucessor(10)) #(9,11)

'''
Passagem de argumentos
'''
def salvar_carro(marca, modelo, ano, placa):
    print(marca, modelo, ano, placa)    

salvar_carro("Fiat", "Doblo", 2000, "123ABC")
salvar_carro(marca="Fiat", modelo="Doblo", ano=2000, placa="123ABC")
# passando um dict **
salvar_carro(**{"marca":"Fiat", "modelo":"Doblo", "ano":2000, "placa":"123ABC"})

# Args(*tupla) e kwargs(**dicionarios)
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema("Sexta, 1 de janeiro 1222", "Zen of Python", autor="Tim Peters", ano=1999,)

