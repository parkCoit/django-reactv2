import os

import numpy as np
from keras.saving.save import load_model
from sklearn import datasets
from tensorboard.compat import tf

"""
Iris Species
Classify dlearn plants into three species in this classic dataset
"""





class IrisService(object):
    def __init__(self):
        global model, graph, target_names
        model = load_model(os.path.join(os.path.abspath("./dlearn/save"), "iris_model.h5"))
        target_names = datasets.load_iris().target_names


    def hook(self):

        ls = [5,5,5,5]
        self.service_model(ls)


    def service_model(self, features):  # features = []
        features = np.reshape(features, (1, 4))
        print(features)
        Y_prob = model.predict(features, verbose=0)
        print(Y_prob)
        predicted = Y_prob.argmax(axis=-1)
        print(predicted)
        return predicted[0]


iris_menu = ["Exit", #0
                "hook"] #1
iris_lambda = {
    "1" : lambda x: x.hook(),
}
if __name__ == '__main__':
    iris = IrisService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                iris_lambda[menu](iris)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")
