import pandas_datareader.data as pdr
import pandas as pd
import os.path as path
import re

def importar_dados(ativos, inicio, fim, nome_arquivo):
    dir_base = path.dirname(__file__)
    dados = pdr.get_data_yahoo(ativos, inicio, fim)
    dados = dados["Close"]
    nomes_colunas = [re.sub(r"\d*-USD", "", simbolo) for simbolo in ativos] # renomeia as colunas
    dados.columns = nomes_colunas
    dados = dados.dropna() # remove linhas sem valor em alguma coluna
    dados.to_csv( path.join(dir_base, nome_arquivo) )

def listar_simbolos():
    with open('../dados/html_yfinance.txt', 'r') as f:
        lines = f.readlines()
    tokens = re.findall(r"p=\S+\"", lines[0])
    resultado = []
    for i in range(len(tokens)):
        tokens[i] = tokens[i].replace('p=', '')
        tokens[i] = tokens[i].replace('"', '')
        if tokens[i] not in resultado:
            resultado.append(tokens[i])
    return resultado  

# BTC a partir de 2018
# ativos = ["BTC-USD"]
# importar_dados(ativos, "2018-01-01", "2021-09-26", "../dados/btc-2018.csv")

# a partir de janeiro de 2018
#ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "LTC-USD"]

# a partir de janeiro de 2021
# ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "ADA-USD", "LINK-USD",  "DOT-USD", "UNI1-USD",
#           "LUNA1-USD", "AVAX-USD", "ALGO-USD", "ATOM-USD", "EGLD-USD", "LTC-USD", "CAKE-USD"]

ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "ADA-USD", "LINK-USD",  "DOT-USD", "UNI1-USD",
          "LUNA1-USD", "AVAX-USD", "ALGO-USD", "ATOM-USD", "EGLD-USD", "LTC-USD", "CAKE-USD",
          'XRP-USD','MATIC-USD','CRO-USD', 'BCH-USD','FTM-USD', 'XLM-USD', 'HBAR-USD', 'MANA-USD', 
          'FTT-USD', 'VET-USD','SAND-USD','FIL-USD','THETA-USD', 'ETC-USD', 'XTZ-USD', 'HNT-USD', 
          'XMR-USD', 'MIOTA-USD','ONE1-USD','AAVE-USD','GRT1-USD','EOS-USD', 'STX-USD','FLOW-USD',
          'LRC-USD', 'BTT-USD','KSM-USD']

importar_dados(ativos, '2021-01-01', '2021-12-31', '../dados/cotacoes-2021-jan-dez.csv')

