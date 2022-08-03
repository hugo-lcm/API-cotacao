import requests
import json
from datetime import datetime


cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL') #atualiza a cada 30s
cotacoes = cotacoes.json()

usd = cotacoes['USDBRL']['bid']
eur = cotacoes['EURBRL']['bid']
btc = cotacoes['BTCBRL']['bid']

now = datetime.now()
current_time = now.strftime(("%H:%M:%S"))

print(f'dólar(USD): R${usd} | atualizado em {current_time}')
print(f'\neuro(EUR): R${eur} | atualizado em {current_time}')
print(f'\nbitcoin(BTC): R${btc} | atualizado em {current_time}')