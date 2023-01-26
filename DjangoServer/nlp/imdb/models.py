import os.path

import keras.utils
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from keras import Sequential, layers, optimizers, callbacks


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

class NaverMovieModel:
    pass







if __name__ == '__main__':
    # data = ImdbService().preprocess()
    # ImdbModel().create(data[0], data[1])
    # ImdbModel().fit(data[2], data[3])
    ImdbModel().hook()
