# -*- coding: utf-8 -*-
'''cryptowatchAPIにて、取得したデータをディープラーニング()'''
import requests
import pandas as pd

def get_data():
    URL = 'https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc'
    response = requests.get(URL)
    print(response)

def main():
    get_data()

if __name__ == '__main__':
    main()
