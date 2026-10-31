import pandas as pd

# Ler a planilha de clientes atendidos
df1 = pd.read_excel("dados.xlsx", sheet_name="Por Canal")

#  Ler planilha com quantidade de pedidos
df2 = pd.read_excel("dados.xlsx", sheet_name="Consumo de Produtos")

# Filtrar categoria desejada
df2 = df2[df2['T. Categoria'].isin(['DRINKS', 'SOFT DRINKS'])]

# calcular total de pessoas atendidas por loja
n_pessoas = df1.groupby('Estabelecimento')['N.Pessoas'].sum()

# calcular quantidades de produtos vendidos por loja e categoria
quant = df2.groupby(['Estabelecimento', 'T. Categoria'])['Quant.'].sum()

# calcular a quantidade de pedidos por cliente
quant_p_pessoas = quant/n_pessoas

print (quant_p_pessoas)