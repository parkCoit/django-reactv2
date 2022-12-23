import os

import numpy as np
from keras.datasets import mnist
from keras.saving.save import load_model



class NumberService(object):

    def service_model(self, i):
        model = load_model(os.path.join(os.path.abspath("./dlearn/save"), "number_model.h5"))
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        print(y_test)
        predictions = model.predict(x_test)
        predictions_array, true_label, img = predictions[i], y_test[i], x_test[i]
        print(predictions_array)
        predicted_label = np.argmax(predictions_array)
        print(predicted_label)
        return str(predicted_label)

if __name__ == '__main__':
    NumberService().service_model(154)