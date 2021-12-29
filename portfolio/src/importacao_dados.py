import pandas_datareader.data as pdr
import pandas as pd
import os.path as path
import re

def importar_dados(ativos, inicio, fim, nome_arquivo):
    dir_base = path.dirname(__file__)
    dados = pdr.get_data_yahoo(ativos, inicio, fim)
    dados = dados["Close"].dropna() # remove linhas sem valor em alguma coluna
    nomes_colunas = [re.sub(r"\d*-USD", "", simbolo) for simbolo in ativos]
    dados.columns = nomes_colunas
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
ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "SOL-USD", "DOT-USD", "UNI1-USD", 
          "LUNA1-USD", "AVAX-USD", "ALGO-USD", "ATOM1-USD", "EGLD-USD", "LTC-USD", "CAKE-USD"]

# ativos = ['BTC-USD','ETH-USD','BNB-USD','SOL-USD','HEX-USD','ADA-USD','XRP-USD','LUNA1-USD','DOT-USD','AVAX-USD',
#           'DOGE-USD','SHIB-USD','MATIC-USD','CRO-USD','UNI1-USD','LTC-USD','LINK-USD','ALGO-USD','BCH-USD',
#           'TRX-USD','XLM-USD','MANA-USD','ATOM-USD','AXS-USD','FTM-USD','VET-USD','FTT-USD','SAND-USD',
#           'HBAR-USD','FIL-USD','THETA-USD','EGLD-USD','ICP-USD','ETC-USD','MIOTA-USD','XTZ-USD','HNT-USD',
#           'XMR-USD','AAVE-USD','GRT1-USD','CAKE-USD','EOS-USD','STX-USD','FLOW-USD','LRC-USD','ONE1-USD',
#           'BTT-USD','KSM-USD','MKR-USD','ENJ-USD']

importar_dados(ativos, "2021-01-01", "2021-12-24", "../dados/cotacoes-2021-jan-dez.csv")

# "XRP"
# "DOGE"
# "SHIB"
# "MATIC"
# "CRO"
# "BCH"
# "NEAR"
# "XLM"
# "MANA"
# "AXS"
# "VET"
# "FTM"
# "FTT"
# "SAND"
# "HBAR"
# "FIL"
# "THETA"