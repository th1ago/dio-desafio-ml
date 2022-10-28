'''
Um set 'e uma colecao que nao possui objetos repetidos
Utilizado para eliminar itens duplicado de um iteravel
'''
import enum


num = set([1, 1, 2, 3, 3, 4])
print(num)

#acessando os valores de um set
numeros = {1,2,3,2}
#transformar ela em uma lista para acessar
listas = list(numeros)
print(listas)

#quando for querer saber o indice
#utiliza a funcao enumerate
carros = {"celta", "hb20", "polo"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")