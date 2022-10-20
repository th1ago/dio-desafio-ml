'''
Intro the pandas libary
'''

#importando a biblioteca panda
import pandas as pd

#ignora linhas com erros - error_bad_lines=True
df = pd.read_csv("C:\\Users\\Thiago\\Documents\\Projetos\\dio-desafio-ml\\Dados\\listadosFundos.csv", encoding="latin-1", sep=';')

#total de linhas e colunas
linhas = df.shape

#somente o nome da coluna
colunas = df.columns

#as ultimas linhas
ulitmas_linhas = df.tail(5)

#retorna estatísticas dos dados
descricao = df.describe()

print(colunas)