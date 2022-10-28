'''
Um set 'e uma colecao que nao possui objetos repetidos
Utilizado para eliminar itens duplicado de um iteravel
'''
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

# union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)

# intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)

# isdisjoint - se eles possuem alguma intersecção
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)

# issuperset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)

# issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)

# symetric_difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)

# difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)