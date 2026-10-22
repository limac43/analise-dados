import pandas as pd

# Ler a planilha de clientes atendidos
df1 = pd.read_excel("dados.xlsx", sheet_name="Por Canal")

#  Ler planilha com quantidade de pedidos
df2 = pd.read_excel("dados.xlsx", sheet_name="Consumo de Produtos")

# Filtrar categoria desejada
df2 = df2[df2['T. Categoria'].isin(['DRINKS', 'SOFT DRINKS'])]


print (df2)