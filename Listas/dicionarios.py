'''
Um conjunto de pares chave:valor
'''

from numpy import NaN

pessoa = {"nome": "Taigo", "idade": NaN}
print(pessoa)

pessoas = dict(nome="taigo", idade=NaN)
print(pessoas)

pessoa["telefone"] = "321-321"
print(pessoa) 

# fromkeys - cria chaves para voce
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}
dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

# setdefault
contato = {"nome": "Taigo", "telefone": 321-321}
# se o atributo nao estiver no dicionario ele adiciona
# se existir ele retorna o valor que esta
contato.setdefault("nome", "Giovanna") # Taigo

