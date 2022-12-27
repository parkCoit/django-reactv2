import os.path

import keras.utils
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from bs4 import BeautifulSoup
from keras import Sequential, layers, optimizers, callbacks
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webcrawler.models import Scrap

from nlp.imdb.services import ImdbService

"""

"""

class ImdbModel(object):
    def __init__(self):
        pass

    def hook(self):
        data = ImdbService().preprocess()
        self.create(data['train_seq'], data['val_seq'])
        self.fit(data['train_target'], data['val_target'])

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
        url = f'https://movie.naver.com/movie/point/af/list.naver?&page=1'
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        file_name = r'C:\Users\bitcamp\django-react\DjangoServer\nlp\imdb\naver_movie_review_corpus.csv'

    def crawling(self):
        if os.path.isfile(file_name):
            review_csv = pd.read_csv(file_name, header=None, index_col=0)
            ls_review = list(review_csv.index)
            print(ls_review)
        else:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_td = soup.find_all('td', attrs={"class" : "title"})


            reviews = {td.br.next_element.strip():td.div.em.text
                        for td  in all_td
                        if td.br.next_element.strip() != ""} # strip()함수는 공백 제거(ex) \n)
            df = pd.Series(reviews)
            print(reviews)
            df.to_csv(file_name, header=None)
            driver.close()
            review_csv = pd.read_csv(file_name, header=None, index_col=0)
            ls_review = list(review_csv.index)
            print(ls_review)


if __name__ == '__main__':
    # data = ImdbService().preprocess()
    # ImdbModel().create(data[0], data[1])
    # ImdbModel().fit(data[2], data[3])
    ImdbModel().hook()
    NaverMovieModel().crawling()
