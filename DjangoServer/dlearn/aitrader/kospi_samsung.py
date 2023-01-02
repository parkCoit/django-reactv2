import os

import numpy as np
import pandas as pd
from keras import Sequential
from keras.callbacks import EarlyStopping
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler

from admin.path import dir_path

from sklearn.model_selection import train_test_split


class KospiSamsung(object):
    def __init__(self):
        pass

    def dataframe_preprocess(self):
        global path ,df1, df2, kospi200, samsung, x, y
        path = dir_path('dlearn')
        df1 = pd.read_csv(os.path.join(path, r'aitrader\kospi200.csv'),
                          index_col=0, header=0, encoding='UTF-8', sep=',').drop('변동 %', axis=1)
        df1 = df1[['오픈', '고가', '저가', '종가', '거래량']]
        df2 = pd.read_csv(os.path.join(path, r'aitrader\samsung.csv'),
                          index_col=0, header=0, encoding='UTF-8', sep=',').drop('변동 %', axis=1).dropna()
        df2 = df2[['오픈', '고가', '저가', '종가', '거래량']]

        for i in range(len(df1.index)):
            df1.iloc[i,4] = float(df1.iloc[i,4].replace('M', '').replace('K', ''))


        for i in range(len(df2.index)):
            for j in range(len(df2.iloc[i])-1):
                df2.iloc[i,j] = int(df2.iloc[i,j].replace(',', ''))
        for i in range(len(df2.index)):
            df2.iloc[i,4] = float(df2.iloc[i,4].replace('M', '').replace('K', ''))


        df1 = df1.values
        df2 = df2.values

        np.save(os.path.join(path, r'aitrader\kospi200.npy'), arr=df1)
        np.save(os.path.join(path, r'aitrader\samsung.npy'), arr=df2)

        kospi200 = np.load(os.path.join(path, r'aitrader\kospi200.npy'),
                           allow_pickle=True)  # allow_pickle False 를 True로 바꿈
        samsung = np.load(os.path.join(path, r'aitrader\samsung.npy'), allow_pickle=True)

        # split 함수 이용하여 5일분 시가,고가,저가,종가
        x, y = self.split_xy5(samsung, 5, 1)



    def show_data(self):
        # print(f'삼성전자 :{df1}')
        # print(df1.shape)
        # print(f'코스피200 : {df2}')
        # print(df2.shape)

        # split_xy5 프린트
        # x, y = self.split_xy5(samsung, 5, 1)
        # print(x[0, :], "\n", y[0])
        # print(x.shape)
        # print(y.shape)
        pass

    def split_xy5(self, dataset, time_steps, y_column):
        x, y = list(), list()
        for i in range(len(dataset)):
            x_end_number = i + time_steps
            y_end_number = x_end_number + y_column

            if y_end_number > len(dataset):
                break
            tmp_x = dataset[i:x_end_number, :].astype(np.float32)
            tmp_y = dataset[x_end_number:y_end_number, 3].astype(np.float32)
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x), np.array(y)

    def dnn_preprocess(self):
        global x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled
        x_train , x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        # standarScaler 에서 2차원으로 받기 때문에 3차원을 2차원으로 바꿔줌
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1]* x_train.shape[2]))
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2]))
        print(x_train.shape)
        print(x_test.shape)

        # StandardScaler() 를 이용한 전처리
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        print(x_train_scaled[0, :])


    def samsung_model(self):
        model = Sequential()
        model.add(Dense(64, input_shape=(25, )))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))

        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)
        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1,
                  batch_size=1, epochs=100, callbacks=[early_stopping])
        print(len(x_train_scaled), len(y_test))
        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        print('loss :', loss)
        print('mse :', mse)

        y_pred = model.predict(x_test_scaled)

        for i in range(5):
            print(f'종가 : {y_test[i]}, / 예측가 : {y_pred[i]}')




if __name__ == '__main__':
    kospisamsung = KospiSamsung()
    kospisamsung.dataframe_preprocess()
    # kospisamsung.show_data()
    kospisamsung.dnn_preprocess()
    kospisamsung.samsung_model()