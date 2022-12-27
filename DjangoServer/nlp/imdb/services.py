from keras.datasets import imdb
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from keras_preprocessing.sequence import pad_sequences

class ImdbService:
    def __init__(self):
        global train_input, train_target, test_input, test_target, val_input, val_input, val_target
        # 데이터 셋 불러오기
        (train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)
        # 20% 를 검증세트로 떼어놓으면 훈련세트는 80%로 줄어듬
        train_input, val_input, train_target, val_target = train_test_split(
            train_input, train_target, test_size=0.2, random_state=42
        )

    def hook(self):
        self.show_data()
        self.create_model()
        self.preprocess()


    def show_data(self):
        print(train_input.shape, test_input.shape)
        print(len(train_input[0]))
        print(len(train_input[1]))
        print(train_input[0])
        print(train_target[:20])
        lengths = np.array([len(x) for x in train_input])  # 각 리뷰의 길이를 계산해 넘파이 배열에 담기
        print(np.mean(lengths), np.median(lengths))  # mean()함수와 median() 함수를 사용해 리뷰 길이의 평균과 중간값 구하기
        plt.hist(lengths)
        plt.xlabel('length')
        plt.ylabel('frequency')
        plt.show()

    def preprocess(self):
        train_seq = pad_sequences(train_input, maxlen=100) # pad_sequences() 함수를 사용해 train_input의 길이를 100으로 맞춘다

        # print(train_seq.shape)
        # print(train_seq[0])
        # print(train_input[0][-10:])
        # print(train_seq[5])
        val_seq = pad_sequences(val_input, maxlen=100)
        return {'train_seq' : train_seq,
                'val_seq': val_seq,
                'train_target': train_target,
                'val_target': val_target}


    def create_model(self):
        pass


