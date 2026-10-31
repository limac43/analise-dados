import pandas as pd
import matplotlib.pyplot as plt

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

# Top 5 produtos por loja e categoria
top5 = df2.groupby(['Estabelecimento', 'Descrição','T. Categoria'])['Quant.'].sum()
top5 = top5.sort_values(ascending=False)
top5 = top5.groupby(['Estabelecimento','T. Categoria']).head(5)
top5 = top5.sort_index()
print(top5)

# plotar grafico para visualizar os resultados
ax = quant_p_pessoas.plot.barh() 
ax.bar_label(ax.containers[0], label_type='edge', fontsize=8) # Adicionar rótulos às barras
ax.set_xlim(0, ax.get_xlim()[1] * 1.1)  # Ajustar o limite do eixo x para melhor visualização
ax.get_xlim()  # Ajustar o limite do eixo x para melhor visualização

plt.tight_layout() # Ajustar o layout para evitar sobreposição de elementos
plt.show()
