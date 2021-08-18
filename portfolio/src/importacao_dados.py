import pandas_datareader.data as pdr
import os.path as path

dir_base = path.dirname(__file__)

# a partir de janeiro de 2018
#ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "LTC-USD"]

# a partir de janeiro de 2021
ativos = ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "LINK-USD", "LTC-USD", "XRP-USD", "SOL1-USD", "DOT1-USD", "BCH-USD"]

# a partir de abril de 2021
#["UNI3-USD", "CAKE-USD", "MATIC-USD"]
inicio = "2021-01-01"
fim = "2021-08-15"

dados = pdr.get_data_yahoo(ativos, inicio, fim)
dados = dados["Close"]
dados.to_csv( path.join(dir_base, '../dados/cotacoes.csv') )