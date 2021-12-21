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

# BTC a partir de 2018
# ativos = ["BTC-USD"]
# importar_dados(ativos, "2018-01-01", "2021-09-26", "../dados/btc-2018.csv")

# a partir de janeiro de 2018
#ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "LTC-USD"]

# a partir de janeiro de 2021
# ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "LTC-USD", "XRP-USD", "SOL1-USD", "DOT1-USD", "BCH-USD"]

# a partir de junho de 2021
ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "SOL-USD", "DOT-USD", "UNI1-USD", "LUNA1-USD", "AVAX-USD", "ALGO-USD", "ATOM1-USD", "EGLD-USD", "LTC-USD"]
importar_dados(ativos, "2021-06-01", "2021-12-20", "../dados/cotacoes-2021-jun-dez.csv")