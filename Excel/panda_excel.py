import pandas as pd

#Leitura dos arquivos
df1 = pd.read_excel("Excel\datasets\Aracaju.xlsx", engine="openpyxl")
df2 = pd.read_excel("Excel\datasets\Fortaleza.xlsx", engine="openpyxl")
df3 = pd.read_excel("Excel\datasets\Recife.xlsx", engine="openpyxl")
df4 = pd.read_excel("Excel\datasets\Natala.xlsx", engine="openpyxl")
df5 = pd.read_excel("Excel\datasets\Salvador.xlsx", engine="openpyxl")

#juntando os arquivos
df = pd.concat([df1, df2])

#alterando o tipo de dado da coluna LojaID
df["LojaId"] = df["LojaID"].astype("object")

#consultando linhas com valores faltantes
df.isnull().sum()

#substituindo linhas com valores faltantes
linhas_faltantes = df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

#substituindo os valores nulos por zero
substituido_zero = df["Vendas"].fillna(0, inplace=True)

#apagando as linhas com valores nulos
nulos = df.dropna(inplace=True)

print(df2.head())
