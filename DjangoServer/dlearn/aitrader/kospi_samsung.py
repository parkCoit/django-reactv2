import os

import numpy as np
import pandas as pd
from keras import Sequential, Input, Model
from keras.callbacks import EarlyStopping
from keras.layers import Dense, LSTM, concatenate
from sklearn.preprocessing import StandardScaler

from admin.path import dir_path

from sklearn.model_selection import train_test_split



class KospiSamsung(object):
    def __init__(self):
        global path, kospi200, samsung
        path = dir_path('dlearn')
        kospi200 = np.load(os.path.join(path, r'aitrader\save\kospi200.npy'),
                           allow_pickle=True)  # allow_pickle False 를 True로 바꿈
        samsung = np.load(os.path.join(path, r'aitrader\save\samsung.npy'), allow_pickle=True)

    def hook(self):
        # self.save_npy()
        self.show_data()
        # self.kospi_scaled()
        # self.samsung_scaled()
        # self.DNN()
        # self.LSTM()
        # self.DNN_Ensemble()
        # self.LSTM_Ensemble()
        # self.dnn_kospi_scaled()

    def save_npy(self):  # df1 = kospi , df2 = samsung

        df1 = pd.read_csv(os.path.join(path, r'aitrader\data\kospi200.csv'),
                          index_col=0, header=0, encoding='UTF-8', sep=',').drop('변동 %', axis=1)
        df1 = df1[['오픈', '고가', '저가', '종가', '거래량']]
        df2 = pd.read_csv(os.path.join(path, r'aitrader\data\samsung.csv'),
                          index_col=0, header=0, encoding='UTF-8', sep=',').drop('변동 %', axis=1).dropna()
        df2 = df2[['오픈', '고가', '저가', '종가', '거래량']]


        for i in range(len(df1.index)):
            if "M" in df1.iloc[i, 4]:
                df1.iloc[i, 4] = df1.iloc[i, 4].replace('M', '')
                df1.iloc[i, 4] = int(float(df1.iloc[i, 4]) * 1000000)
            elif "K" in df1.iloc[i, 4]:
                df1.iloc[i, 4] = df1.iloc[i, 4].replace('K', '')
                df1.iloc[i, 4] = int(float(df1.iloc[i, 4]) * 1000)


        for i in range(len(df2.index)):
            for j in range(len(df2.iloc[i])):
                if ',' in df2.iloc[i, j]:
                    df2.iloc[i, j] = int(df2.iloc[i, j].replace(',', ''))
                elif "M" in df2.iloc[i, j]:
                    df2.iloc[i, j] = df2.iloc[i, j].replace('M', '')
                    df2.iloc[i, j] = int(float(df2.iloc[i, j]) * 1000000)
                elif "K" in df2.iloc[i, j]:
                    df2.iloc[i, j] = df2.iloc[i, j].replace('K', '')
                    df2.iloc[i, j] = int(float(df2.iloc[i, j]) * 1000)


        df1 = df1.values
        df2 = df2.values

        np.save(os.path.join(path, r'aitrader\save\kospi200.npy'), arr=df1)
        np.save(os.path.join(path, r'aitrader\save\samsung.npy'), arr=df2)


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

    def dnn_samsung_scaled(self):
        x, y = self.split_xy5(samsung, 5, 1)  # 삼성

        x_train , x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        # standarScaler 에서 2차원으로 받기 때문에 3차원을 2차원으로 바꿔줌
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test = y_test.astype(float)

        print(x_train.shape)
        print(x_test.shape)

        # StandardScaler() 를 이용한 전처리
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        print(x_train_scaled[0, :])

        return x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled

    def LSTM_samsung_scaled(self):
        x, y = self.split_xy5(samsung, 5, 1)  # 삼성

        x_train , x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        # standarScaler 에서 2차원으로 받기 때문에 3차원을 2차원으로 바꿔줌
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test = y_test.astype(float)

        print(x_train.shape)
        print(x_test.shape)

        # StandardScaler() 를 이용한 전처리
        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train_scaled = scaler.transform(x_train)
        x_test_scaled = scaler.transform(x_test)
        print(x_train_scaled[0, :])


        x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0], 5, 5)) # LSTM 사용할때 3차원으로 다시
        x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0], 5, 5))


        return x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled

    def dnn_kospi_scaled(self):
        x2, y2 = self.split_xy5(kospi200, 5, 1)

        x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=1, test_size=0.3)
        x2_train = np.reshape(x2_train, (x2_train.shape[0], x2_train.shape[1] * x2_train.shape[2])).astype(float)
        x2_test = np.reshape(x2_test, (x2_test.shape[0], x2_test.shape[1] * x2_test.shape[2])).astype(float)
        y2_train = y2_train.astype(float)
        y2_test = y2_test.astype(float)

        print(x2_train.shape)
        print(x2_test.shape)

        # StandardScaler() 를 이용한 전처리
        scaler = StandardScaler()
        scaler.fit(x2_train)
        x2_train_scaled = scaler.transform(x2_train)
        x2_test_scaled = scaler.transform(x2_test)
        print(x2_train_scaled[0, :])

        return x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled

    def LSTM_kospi_scaled(self):
        x2, y2 = self.split_xy5(kospi200, 5, 1)

        x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=1, test_size=0.3)
        x2_train = np.reshape(x2_train, (x2_train.shape[0], x2_train.shape[1] * x2_train.shape[2])).astype(float)
        x2_test = np.reshape(x2_test, (x2_test.shape[0], x2_test.shape[1] * x2_test.shape[2])).astype(float)
        y2_train = y2_train.astype(float)
        y2_test = y2_test.astype(float)

        print(x2_train.shape)
        print(x2_test.shape)

        # StandardScaler() 를 이용한 전처리
        scaler = StandardScaler()
        scaler.fit(x2_train)
        x2_train_scaled = scaler.transform(x2_train)
        x2_test_scaled = scaler.transform(x2_test)
        print(x2_train_scaled[0, :])

        x2_train_scaled = np.reshape(x2_train_scaled, (x2_train_scaled.shape[0], 5, 5))  # LSTM 사용할때 3차원으로 다시
        x2_test_scaled = np.reshape(x2_test_scaled, (x2_test_scaled.shape[0], 5, 5))

        return x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled



    def DNN(self):    # dnn_preprocess 2차원으로 변경
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.dnn_samsung_scaled()

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
        model.save(f'{path}\\aitrader\\save\\DNN.h5')
        print('loss :', loss)
        print('mse :', mse)

        y_pred = model.predict(x_test_scaled)

        for i in range(5):
            print(f'종가 : {y_test[i]}, / 예측가 : {y_pred[i]}')

    def LSTM(self):   # dnn_preprocess 3차원으로 변경
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.LSTM_samsung_scaled()
        print(x_train_scaled.shape)
        print(x_test_scaled.shape)
        model = Sequential()
        model.add(LSTM(64, input_shape=(5, 5)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)

        model.fit(x_train_scaled, y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate(x_test_scaled, y_test, batch_size=1)
        model.save(f'{path}\\aitrader\\save\\LSTM.h5')
        print('loss : ', loss)
        print('mse: ', mse)

        y_pred = model.predict(x_test_scaled)

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')

    def DNN_Ensemble(self):   # dnn_preprocess 2차원으로 변경
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.dnn_samsung_scaled()
        x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled = self.dnn_kospi_scaled()

        input1 = Input(shape=(25,))
        dense1 = Dense(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(25,))
        dense2 = Dense(64)(input2)
        dense2 = Dense(32)(dense2)
        dense2 = Dense(32)(dense2)
        output2 = Dense(32)(dense2)

        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)
        model = Model(inputs=[input1, input2], outputs=output3)

        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)

        model.fit([x_train_scaled, x2_train_scaled], y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate([x_test_scaled, x2_test_scaled], y_test, batch_size=1)
        model.save(f'{path}\\aitrader\\save\\DNN_Ensemble.h5')
        print('loss : ', loss)
        print('mse: ', mse)

        y_pred = model.predict([x_test_scaled, x2_test_scaled])

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')

    def LSTM_Ensemble(self):
        x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = self.LSTM_samsung_scaled()
        x2_train, x2_test, y2_train, y2_test, x2_train_scaled, x2_test_scaled = self.LSTM_kospi_scaled()

        input1 = Input(shape=(5, 5))
        dense1 = LSTM(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(5, 5))
        dense2 = LSTM(64)(input2)
        dense2 = Dense(64)(dense2)
        dense2 = Dense(64)(dense2)
        output2 = Dense(32)(dense2)

        merge = concatenate([output1, output2])
        output3 = Dense(1)(merge)
        model = Model(inputs=[input1, input2], outputs=output3)

        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)

        model.fit([x_train_scaled, x2_train_scaled], y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate([x_test_scaled, x2_test_scaled], y_test, batch_size=1)
        model.save(f'{path}\\aitrader\\save\\LSTM_Ensemble.h5')
        print('loss : ', loss)
        print('mse: ', mse)

        y_pred = model.predict([x_test_scaled, x2_test_scaled])

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')





if __name__ == '__main__':
    kospisamsung = KospiSamsung()
    kospisamsung.hook()