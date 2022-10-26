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

'''
Trabalhando com colunas=
'''
#criando um nova coluna Receita
#mul() - multiplicacao
df["Receita"] = df["Vendas"].mul(df["Qtde"])

#Retornando a maior receita
df["Receita"].max()

#Retornando a maenor receita
df["Receita"].min()

#Retorna o Top3 da coluna Receita
df.nlargest(3, "Receita")

#Retorna as 3 piores da coluna Receitas
df.nsmallest(3, "Receita")

#Agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()

#Ordenando o conjunto de dados
#ascending - do maior para o menor
df.sort_values("Receita", ascending=False).head(10)

'''
Trabalhando com datas
'''
#transformando a coluna de date em tipo inteiro
df["Data"] = df["Data"].astype("int64")

#verificando o tipo de dado dde cada coluna
df.dtypes

#transformando coluna de date em date
df["Data"] = pd.to_datetime(df["Data"])

#criando uma coluna por ano
#dt = DATETIME
df["Ano_Venda"] = df["Data"].dt.year

'''
Visualizando de dados
'''
#value_counts realiza uma contagem 
#significa que a loja X realizou X vendas
df["LojaID"].value_counts(ascending=False)

#grafico de barras
df["LojaID"].value_counts(ascending=False).plot.bar()
