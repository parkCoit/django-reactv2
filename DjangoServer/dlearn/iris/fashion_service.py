import os.path

import matplotlib.pyplot as plt
import numpy as np
from keras.saving.save import load_model
from sklearn import datasets
from tensorboard.compat import tf
import keras.datasets.fashion_mnist

"""
Iris Species
Classify dlearn plants into three species in this classic dataset
"""





class FashionService(object):
    def __init__(self):
        global class_names, model
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat'
            , 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
        model = None



    # self, i, predictions_array, true_label, img
    def service_model(self, i) -> []:
        model = load_model(os.path.join(os.path.abspath("./dlearn/save"), "fashion_model.h5"))
        (train_images, train_labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
        print(test_labels)
        predictions = model.predict(test_images)
        predictions_array, true_label, img = predictions[i], test_labels[i], test_images[i]
        print(predictions_array)
        # plt.grid(False)
        # plt.xticks([])
        # plt.yticks([])
        # plt.imshow(img, cmap=plt.cm.binary)
        predicted_label = np.argmax(predictions_array)
        print(class_names[predicted_label])
        # if predicted_label == true_label:
        #     color = 'blue'
        # else: color = 'red'
        # plt.xlabel('{} {:2.0f}% ({})'.format(
        #     class_names[predicted_label],
        #     100 * np.max(predictions_array),
        #     class_names[true_label]
        # ), color=color)
        return class_names[predicted_label]




fashion_menu = ["Exit", #0
                "service_model"] #1
fashion_lambda = {
    "1" : lambda x: x.service_model(13),
}
if __name__ == '__main__':
    fashion = FashionService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(fashion_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                fashion_lambda[menu](fashion)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")
