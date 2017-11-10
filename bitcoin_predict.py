# -*- coding: utf-8 -*-
'''cryptowatchAPIにて、取得したデータをディープラーニング()'''
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_data(time=300):
    URL = 'https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods='
    response = requests.get(URL, time).json()
    df_order = pd.DataFrame(response['result'][str(time)])
    df_order.columns = ['CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume']
    return df_order

def split_data(df_chart):
    '''
        CloseTimeとClosePriceのみのndarrayを返す
    '''
    np_chart = df_chart.as_matrix()
    np_return = np_chart[:, 0:5:4]
    return np_return

def create_mean(df_chart, mean=[5, 20]):
    close_chart = np.array(list(df_chart['ClosePrice']))
    max_length = close_chart.shape[0] - max(mean)
    np_return = np.empty([max_length, len(mean)])

    # 平均線の個数だけ繰り返し
    for i, period in enumerate(mean):
        for idx in range(max_length):
            mean_chart = 0
            for j in range(period):
                mean_chart += close_chart[period + idx - j - 1]
            mean_chart /= period
            devarge_chart = close_chart[period + idx - 1] / mean_chart
            np_return[idx, i] = devarge_chart * 100
    return np_return

def plt_show(df_chart):
    xlist = df_chart['CloseTime']
    ylist = df_chart['ClosePrice']
    plt.plot(xlist, ylist)
    plt.show()

def main():
    df_order = get_data()
    np_split = split_data(df_order)
    np_mean = create_mean(df_order)

if __name__ == '__main__':
    main()
