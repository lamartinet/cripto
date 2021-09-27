import pandas_datareader.data as pdr
import os.path as path

dir_base = path.dirname(__file__)

# a partir de janeiro de 2018
#ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "LTC-USD"]

# a partir de janeiro de 2021
# ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "LTC-USD", "XRP-USD", "SOL1-USD", "DOT1-USD", "BCH-USD"]

# a partir de abril de 2021
ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "SOL1-USD", "DOT1-USD", "UNI3-USD", "LUNA1-USD", "AVAX-USD", "ALGO-USD", "ATOM1-USD", "EGLD-USD", "AAVE-USD", "COMP-USD"]


# BTC a partir de dezembro de 2017
# ativos = ["BTC-USD"]


# a partir de abril de 2021
#["UNI3-USD", "CAKE-USD", "MATIC-USD"]
# inicio = "2021-01-01"
# fim = "2021-08-15"
inicio = "2021-04-01"
fim = "2021-09-26"

dados = pdr.get_data_yahoo(ativos, inicio, fim)
dados = dados["Close"]
dados.to_csv( path.join(dir_base, '../dados/cotacoes-2021-abril-setembro.csv') )