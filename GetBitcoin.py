import requests
from datetime import datetime
import pandas as pd

# URL para ter o preço da Bitcoin
url = "https://api.coinbase.com/v2/prices/spot"

# Requisição GET para a API
response = requests.get(url)
data = response.json()

# Extrair os dados que eu quero
preco = float(data['data']['amount'])
ativo = data['data']['base']
moeda = data['data']['currency']
horario_de_coleta = datetime.now()

dataframe = pd.DataFrame({
    'ativo': [ativo],
    'moeda': [moeda],
    'preco': [preco],
    'horario_de_coleta': [horario_de_coleta]  
})