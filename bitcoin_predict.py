# -*- coding: utf-8 -*-
'''cryptowatchAPIにて、取得したデータをディープラーニング()'''
import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_data(time=300):
    URL = 'https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods='
    response = requests.get(URL, time).json()
    df_order = pd.DataFrame(response['result'][str(time)])
    df_order.columns = ['CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume']
    print(df_order.head(20))
    return df_order

def df_to_np(df_data):
    pass

def plt_show(df_data):
    xlist = df_data['CloseTime']
    ylist = df_data['ClosePrice']
    plt.plot(xlist, ylist)
    plt.show()

def main():
    df_order = get_data()
    np_order = df_to_np(df_order)
    plt_show(df_order)

if __name__ == '__main__':
    main()
