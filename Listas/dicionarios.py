'''
Um conjunto de pares chave:valor
'''

from numpy import NaN

pessoa = {"nome": "Thiago", "idade": NaN}
print(pessoa)

pessoas = dict(nome="thiago", idade=NaN)
print(pessoas)

pessoa["telefone"] = "321-321"
print(pessoa) 