import keras.utils
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from bs4 import BeautifulSoup
from keras import Sequential, layers, optimizers, callbacks
from selenium import webdriver
from webcrawler.models import Scrap

from nlp.imdb.services import ImdbService

"""

"""

class ImdbModel(object):
    def __init__(self):
        pass

    def hook(self):
        data = ImdbService().preprocess()
        self.create(data[0], data[1])
        self.fit(data[2], data[3])

    def create(self, train_seq, val_seq):
        global model ,train_oh, val_oh
        model = Sequential()
        sample_length = 100
        freq_words = 500
        model.add(layers.SimpleRNN(8, input_shape=(sample_length, freq_words)))
        model.add(layers.Dense(1, activation='sigmoid'))
        train_oh = keras.utils.to_categorical(train_seq) # oh is OneHotEncoding
        print(train_oh)
        print(train_oh[0][0][:12])
        val_oh = keras.utils.to_categorical(val_seq)


    def fit(self, train_target, val_target):
        rmsprop = optimizers.RMSprop(learning_rate=1e-4)
        model.compile(optimizer=rmsprop, loss='binary_crossentropy',
                      metrics=['accuracy'])
        checkpoint_cb = callbacks.ModelCheckpoint('best-simplernn-model.h5',
                                                  save_best_only=True)
        early_stopping_cb = callbacks.EarlyStopping(patience=3,restore_best_weights=True)
        history = model.fit(train_oh, train_target, epochs=100, batch_size=64,
                            validation_data=(val_oh, val_target),
                            callbacks=[checkpoint_cb, early_stopping_cb])
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend(['train', 'val'])
        plt.show()


class NaverMovieModel(Scrap):
    def __init__(self):
        global url, driver, file_name
        url = 'https://movie.naver.com/movie/point/af/list.naver?&page=1'
        driver = webdriver.Chrome(executable_path='C:/Users/bitcamp/django-react/DjangoServer/webcrawler/chromedriver.exe')
        file_name = r'C:\Users\bitcamp\django-react\DjangoServer\nlp\imdb\naver_movie_review_corpus.csv'

    def crawling(self):
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_divs = soup.find_all('td', attrs={"class" : "title"})
        products = [div1.br.next_element.strip() for div1 in all_divs] # strip()함수는 공백 제거(ex) \n)
        df = pd.Series(products)
        df.index = df.index + 1
        df.to_csv(file_name, header=None, index=None)
        driver.close()
        review_csv = pd.read_csv(file_name)
        print(review_csv)


if __name__ == '__main__':
    # data = ImdbService().preprocess()
    # ImdbModel().create(data[0], data[1])
    # ImdbModel().fit(data[2], data[3])
    NaverMovieModel().crawling()
