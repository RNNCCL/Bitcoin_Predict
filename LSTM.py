# -*- coding: utf-8 -*-
'''cryptowatchAPIにて、取得したデータをディープラーニング（）'''
import requests
import pandas as pd

def get_data(time=300):
    URL = 'https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods='
    response = requests.get(URL, time).json()
    df_order = pd.DataFrame(response['result'][str(time)])
    df_order.columns = ['CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume']
    return df_order

def main():
    # 変数
    TIME = 300

    df_order = get_data(time=TIME)

if __name__ == '__main__':
    main()
