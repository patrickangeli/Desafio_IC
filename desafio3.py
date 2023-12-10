import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

# Carregar o arquivo Excel para um DataFrame
df = pd.read_excel('vendas.xlsx')

# Converter a coluna 'Data_Hora' para o formato de data
df['Data_Hora'] = pd.to_datetime(df['Data_Hora'], format='%d/%m/%Y %H:%M')

# Adicionar colunas para o ano
df['Ano'] = df['Data_Hora'].dt.year

# Selecionar as colunas relevantes para o modelo
X = df[['Ano', 'Num_vendas']]
y = df['Num_vendas']

# Normalizar/Padronizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Separar em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.8, random_state=42)

# Extrair o alvo (vendas) para treino e teste
y_train = X_train[:, 1]  # Num_vendas
y_test = X_test[:, 1]    # Num_vendas

# Criar e treinar o modelo de rede neural
model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Criar e treinar o modelo de rede neural
dados_previsao = pd.DataFrame({'Ano': [2019,2020,2021,2022], 'Num_vendas':[0,0,0,0]})
dados_previsao_scaled = scaler.transform(dados_previsao[['Ano', 'Num_vendas']])

# Criar dados para os anos de 2018 e 2019
#dados_previsao = pd.DataFrame({'Ano': [2017, 2019], 'Num_vendas': [0, 0]})
#dados_previsao_scaled = scaler.transform(dados_previsao[['Ano', 'Num_vendas']])

# Fazer previsões para os anos de 2018 e 2019
previsoes = model.predict(dados_previsao_scaled)


# Imprimir as previsões
for i in range(len(previsoes)):
  ano_previsto = dados_previsao['Ano'].iloc[i]
  valor_previsto = previsoes[i]*(-1)
  print(f"A acurácia para o ano de {ano_previsto} é de {valor_previsto}")
print ('Valor previsto ', valor_previsto)