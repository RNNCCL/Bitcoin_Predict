# -*- coding: utf-8 -*-
'''cryptowatchAPIにて、取得したデータをディープラーニング()'''
import requests
import pandas as pd

def get_data(time=300):
    URL = 'https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods='
    response = requests.get(URL, time).json()
    df_order = pd.DataFrame(response['result'][str(time)])
    df_order.columns = ['CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume']
    print(df_order.head(20))

def main():
    get_data()

if __name__ == '__main__':
    main()
