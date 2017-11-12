# -*- coding: utf-8 -*-
'''cryptowatchAPIにて、取得したデータをRandomForest'''
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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

def create_mean(np_chart, mean=[5, 20]):
    close_chart = np_chart[:, 1]
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

def create_y(np_split, p=0.1):
    np_y = np.empty((0, 1), float)
    np_return = np.empty((0, 1), int)
    for i in range(1, np_split.shape[0]):
        np_y = np.append(np_y, np_split[i, 1] / np_split[i - 1, 1] * 100)
    for yi in np_y:
        if yi > 100 + p:
            np_return = np.append(np_return, 1)
        elif yi < 100 - p:
            np_return = np.append(np_return, -1)
        else:
            np_return = np.append(np_return, 0)
    return np_return

def plt_show(df_chart):
    xlist = df_chart['CloseTime']
    ylist = df_chart['ClosePrice']
    plt.plot(xlist, ylist)
    plt.show()

def main():
    # 変数
    MEAN = [5, 10]
    P = 0
    TIME = 300

    # データの整理
    df_order = get_data(time=TIME)
    np_split = split_data(df_order)
    np_mean = create_mean(np_split, mean=MEAN)
    np_y = create_y(np_split, p=P)
    np_y = np_y[max(MEAN)-1:]

    # 機械学習するやーつ
    X_train, X_test, y_train, y_test = train_test_split(np_mean, np_y, test_size=0.3)
    forest = RandomForestClassifier(criterion='entropy', n_estimators=100)
    forest.fit(X_train, y_train)
    y_predict = forest.predict(X_test)
    print("正答率: ", accuracy_score(y_test, y_predict))

    # 描画
    plt_show(df_order)

if __name__ == '__main__':
    main()
