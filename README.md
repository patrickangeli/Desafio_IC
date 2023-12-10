# Desafio_IC 

## Desafio 1
Para realizar a leitura da página e procurar nela os elementos, utilizei o BeautifulSoap, mesmo a pagina sendo em FTP, sua construção foi feita em HTML, desta forma precisava de utilizar uma ferramenta capaz de ler os elementos em HTML. Procurei primeiro pelo elemento que inicia o parametro no HTML, por fim utilizei o endswitch para realizar a busca da extensão pretendida.

Os parâmetros de entrada da função ```download_files(base_url, save_path)```, na qual ```base_url``` é o site de entrada e o ```save_path```é o local que irá salvar os arquivos.

## Desafio 2
A entrada é um arquivo de extensão ```.xlsx```, popdendno ser alterado na linha 9 ```df = pd.read_excel('vendas.xlsx')```. Separei a coluna data em dia, mês e ano, para poder facilitar as analises.

Desta forma, fiz analises de media, número maximo e minimo de vendas e mediana.

Plotei gráficos com as médias, linha de tendência e volume máximo de cada ano. O próximo gráfico é uma linha mostrando os máximos de cada ano de produção.

## Desafio 3

Para poder fazer a rede neural utilizei regressão linear simples, dado que para alimentar a rede neural utilizei dois vetores, um dos dias juntamente com os horários.

Como são duas métricas simples não vi necessidade de usar uma rede neural mais complexa, com mais camadas que essa.

Utilizei o MLPRegressor com 100 neurônios com 50 camadas. Para fazer a validação utilizei como treino 80% e os outros 20% restante para teste.

```
model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.8, random_state=42)

```

Escalei o ```Num_vendas``` para poder fazer a predição esperada em vendas.

O modelo teve um aprendizado satisfatório, dado que teve uma taxa de aprendizagem alta, conforme mostrado em resultados.
