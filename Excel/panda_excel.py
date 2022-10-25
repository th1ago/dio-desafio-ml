import pandas as pd

#Leitura dos arquivos
df1 = pd.read_excel("Excel\datasets\Aracaju.xlsx", engine="openpyxl")
df2 = pd.read_excel("Excel\datasets\Fortaleza.xlsx", engine="openpyxl")
df3 = pd.read_excel("Excel\datasets\Recife.xlsx", engine="openpyxl")
df4 = pd.read_excel("Excel\datasets\Natala.xlsx", engine="openpyxl")
df5 = pd.read_excel("Excel\datasets\Salvador.xlsx", engine="openpyxl")

#juntando os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

#alterando o tipo de dado da coluna LojaID
df["LojaId"] = df["LojaID"].astype("object")

#consultando linhas com valores faltantes
df.isnull().sum()

#substituindo linhas com valores faltantes
#mean() - media
linhas_faltantes = df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

#substituindo os valores nulos por zero
substituindo_zero = df["Vendas"].fillna(0, inplace=True)

#apagando as linhas com valores nulos
nulos = df.dropna(inplace=True)

#apagando as linhas com valores nulos com base em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)

#removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

print(df.head())

#Criando nova coluna de receita
#criando coluna Receita
#mul() - multiplicacao
df["Receita"] = df["Vendas"].mul(df["Qtde"])

#Retornando a maior receita
df["Receita"].max()

#Retornando a maenor receita
df["Receita"].min()
