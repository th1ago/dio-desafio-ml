import pandas as pd

#Leitura dos arquivos
df1 = pd.read_excel("Excel\datasets\Aracaju.xlsx", engine="openpyxl")
df2 = pd.read_excel("Excel\datasets\Fortaleza.xlsx", engine="openpyxl")

print(df2.head())
