import os.path
import warnings

import pandas as pd
from keras.saving.save import load_model
from prophet import Prophet

from admin.path import dir_path
from dlearn.aitrader.kospi_samsung import KospiSamsung

warnings.filterwarnings("ignore")
import pandas_datareader.data as web
from pandas_datareader import data
import yfinance as yf
yf.pdr_override() # TypeError: string indices must be integers 해결법
path = "c:/Windows/Fonts/malgun.ttf"
import platform
from matplotlib import font_manager, rc, pyplot as plt

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

plt.rcParams['axes.unicode_minus'] = False

'''
Date  Open   High   Low  Close  Adj Close  Volume

'''

class AiTraderService(object):

    def __init__(self):
        global start_date, end_date, item_code
        start_date = "2020-1-4"
        end_date = "2022-12-31"
        item_code = '000270.KS'

    def kia_predict(self):
        item = data.get_data_yahoo(item_code, start_date, end_date)
        print(f" KIA head : {item.head(3)}"
              f" KIA tail : {item.tail(3)}")
        item['Close'].plot(figsize=(12,6), grid=True)
        item_trunc = item[:'2023-02-20']
        df = pd.DataFrame({'ds' : item_trunc.index, 'y' : item_trunc['Close']})
        df.reset_index(inplace=True)
        del df['Date']
        prophet = Prophet(daily_seasonality=True)
        prophet.fit(df)
        future = prophet.make_future_dataframe(periods=61)
        forecast = prophet.predict(future)
        prophet.plot(forecast)
        plt.figure(figsize=(12,6))
        plt.plot(item.index, item['Close'], label='real')
        plt.plot(forecast['ds'], forecast['yhat'], label='forecast')
        plt.grid()
        path = dir_path('dlearn')
        print(f"path : {path}")
        plt.legend()
        plt.savefig(os.path.join(path, r'aitrader\kia.png'))
        plt.show()

    def DNN_predict(self, i):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = KospiSamsung().dnn_samsung_scaled()

        DNN_model = load_model(os.path.join(os.path.abspath("./dlearn/aitrader/save"), "DNN.h5"))

        y_pred = DNN_model.predict(x_test_scaled)

        return f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}'

    def DNN_Ensemble_predict(self, i):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = KospiSamsung().dnn_samsung_scaled()
        x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled = KospiSamsung().dnn_kospi_scaled()

        DNN_Ensemble_model = load_model(os.path.join(os.path.abspath("./dlearn/aitrader/save"), "DNN_Ensemble.h5"))

        y_pred = DNN_Ensemble_model.predict([x_test_scaled, x2_test_scaled])

        return f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}'

    def LSTM_predict(self, i):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = KospiSamsung().LSTM_samsung_scaled()

        LSTM_model = load_model(os.path.join(os.path.abspath("./dlearn/aitrader/save"), "LSTM.h5"))

        y_pred = LSTM_model.predict(x_test_scaled)

        return f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}'

    def LSTM_Ensemble_predict(self, i):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = KospiSamsung().LSTM_samsung_scaled()
        x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled = KospiSamsung().LSTM_kospi_scaled()

        LSTM_Ensemble_model = load_model(os.path.join(os.path.abspath("./dlearn/aitrader/save"), "LSTM_Ensemble.h5"))

        y_pred = LSTM_Ensemble_model.predict([x_test_scaled, x2_test_scaled])

        return f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}'

if __name__ == '__main__':
    ai = AiTraderService()
    ai.kia_predict()