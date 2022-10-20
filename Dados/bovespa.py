'''
Intro the pandas libary
'''

#NaaN = sao valores nulos
#mean() = media
#sum() = soma

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

#retorna apenas os valores unicos
razao = df["Razao Social"].unique()
segmento = df["Segmento"].unique()
codigo = df["Codigo"].unique()
fundo = df["Fundo"].unique()

#fazer um filtro utilizando o loc
filtro = df.loc[df["Segmento"] == "CYCR"] 

#GroupBy
grupo = df.groupby("Razao Social")["Segmento"].nunique

print(filtro)