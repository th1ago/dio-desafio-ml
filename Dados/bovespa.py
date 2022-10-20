#importando a biblioteca panda
import pandas as pd

df = pd.read_csv("C:\\Users\\Thiago\\Documents\\Projetos\\dio-desafio-ml\\Dados\\listadosFundos.csv", encoding="latin-1", sep=';')
df.head()

print(df)