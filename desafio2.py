#@title Desafio 2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs('Saida/desafio02', exist_ok=True)

# Carregar o arquivo CSV para um DataFrame
df = pd.read_excel('vendas.xlsx')

# Converter a coluna 'Data_Hora' para o formato de data
df['Data_Hora'] = pd.to_datetime(df['Data_Hora'], format='%d/%m/%Y %H:%M')

# Adicionar colunas para o dia, mês e ano
df['Dia'] = df['Data_Hora'].dt.day
df['Mês'] = df['Data_Hora'].dt.month
df['Ano'] = df['Data_Hora'].dt.year

#Calcular a média geral
media = df['Num_vendas'].median().round(2)
mediana = df['Num_vendas'].mean().round(2)
numero_max = df['Num_vendas'].max()
numero_min = df['Num_vendas'].min()

# Calcular a média para cada dia, mês e ano
media_por_ano = df.groupby(['Ano'])['Num_vendas'].median().reset_index()
maximo_por_ano = df.groupby(['Ano'])['Num_vendas'].max().reset_index()
media_por_ano = media_por_ano['Num_vendas'].round(2)
max_dia = df.groupby(['Mês'])['Num_vendas'].max().reset_index()
# Mostrar a média por dia
anos = [2015, 2016, 2017]
with open('Saida/desafio02/output.txt', 'w') as f:
    f.write(f'Media Geral: {media}\n')
    f.write(f'Mediana Geral: {mediana} \n')
    f.write(f'Maior numero: {numero_max}\n')
    f.write(f'Menor número: {numero_min}\n')
    f.write('Media por ano:\n')
    f.write(media_por_ano.to_string(index=False, header=True) + '\n')
    f.write('Maximo por ano:\n')
    f.write(maximo_por_ano.to_string(index=False, header=True) + '\n')


cores = ['blue', 'green', 'orange', 'red']

# Plotar as barras com cores diferentes
plt.bar(anos, media_por_ano, color=cores)
# Adicionar rótulos e título ao gráfico
plt.xlabel('Ano')
plt.ylabel('Número de Vendas')
plt.title('Média de Vendas por Ano')



# Salvar o gráfico como um arquivo PNG
plt.savefig('Saida/desafio02/grafico_vendas_por_ano.png')

plt.plot(maximo_por_ano['Ano'], maximo_por_ano['Num_vendas'], 'o-', label='Máximo por Ano')

plt.xlabel('Ano')
plt.ylabel('Número de Vendas')
plt.title('Máximo de Vendas por Ano')

plt.savefig('Saida/desafio02/maximo_vendas_por_ano.png')


