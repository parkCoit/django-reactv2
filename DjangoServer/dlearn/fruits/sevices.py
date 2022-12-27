import numpy as np
import matplotlib.pyplot as plt


import tensorflow as tf
from tensorflow import keras
from keras.callbacks import ModelCheckpoint
import tensorflow_datasets as tfds


class FruitsService:
    def __init__(self):
        global trainpath, testpath, Apple_Braeburn_Train, Apple_Crimson_Snow_Train, Apple_Golden_1_Train\
            , Apple_Golden_2_Train, Apple_Golden_3_Train, Apple_Braeburn_Test, Apple_Crimson_Snow_Test\
            , Apple_Golden_1_Test, Apple_Golden_2_Test, Apple_Golden_3_Test\
            , batch_size, img_height, img_width, num_classes, epochs
        trainpath = "C:/Users/bitcamp/django-react/DjangoServer/dlearn/fruits/fruits-360-5/Training"
        testpath = "C:/Users/bitcamp/django-react/DjangoServer/dlearn/fruits/fruits-360-5/Test"
        Apple_Braeburn_Train = f"{trainpath}/Apple Braeburn"
        Apple_Crimson_Snow_Train = f"{trainpath}/Apple Crimson Snow"
        Apple_Golden_1_Train = f"{trainpath}/Apple Golden 1"
        Apple_Golden_2_Train = f"{trainpath}/Apple Golden 2"
        Apple_Golden_3_Train = f"{trainpath}/Apple Golden 3"
        Apple_Braeburn_Test = f"{testpath}/Apple Braeburn"
        Apple_Crimson_Snow_Test = f"{testpath}/Apple Crimson Snow"
        Apple_Golden_1_Test = f"{testpath}/Apple Golden 1"
        Apple_Golden_2_Test = f"{testpath}/Apple Golden 2"
        Apple_Golden_3_Test = f"{testpath}/Apple Golden 3"
        batch_size = 32
        img_height = 100
        img_width = 100
        num_classes = 5
        epochs = 20



    def hook(self):
        # self.show_apple()
        # self.create_train_dataset()
        # self.create_test_dataset()
        # self.create_test_dataset_shuffle()
        self.create_model()

    def show_apple(self):
        img = tf.keras.preprocessing.image.load_img \
            (f'{Apple_Golden_3_Train}/0_100.jpg')
        plt.imshow(img)
        plt.axis("off")
        plt.show()

    def create_train_dataset(self):
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            trainpath,
            validation_split=0.3,
            subset="training",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)
        class_names = train_ds.class_names
        print(class_names)
        return [train_ds,class_names]

    def create_validations_dataset(self):
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            trainpath,
            validation_split=0.3,
            subset="validation",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)
        return val_ds


    def create_test_dataset(self):
        class_names = self.create_train_dataset()[1]
        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
            testpath,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)
        print(type(test_ds))
        y = np.concatenate([y for x, y in test_ds], axis=0)
        x = np.concatenate([x for x, y in test_ds], axis=0)
        print(x[0])
        print(y)
        plt.figure(figsize=(3, 3))
        plt.imshow(x[0].astype("uint8"))
        plt.title(class_names[y[0]])
        plt.axis("off")
        plt.show()
        return test_ds

    def create_test_dataset_shuffle(self):
        test_ds = self.create_test_dataset()
        train_ds = self.create_train_dataset()[0]
        class_names = self.create_train_dataset()[1]
        val_ds = self.create_validations_dataset()
        BUFFER_SIZE = 10000

        AUTOTUNE = tf.data.experimental.AUTOTUNE
        test_ds1 = tf.keras.preprocessing.image_dataset_from_directory(
            testpath,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size,
            shuffle=False)
        y = np.concatenate([y for x, y in test_ds1], axis=0)
        x = np.concatenate([x for x, y in test_ds1], axis=0)
        # print(x[0])
        # print(y)
        # plt.figure(figsize=(3, 3))
        # plt.imshow(x[-1].astype("uint8"))
        # plt.title(class_names[y[-1]])
        # plt.axis("off")
        # plt.show()

        train_ds = train_ds.cache().shuffle(BUFFER_SIZE).prefetch(buffer_size=AUTOTUNE)
        val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)
        print(type(train_ds))
        return [train_ds,  val_ds, test_ds]


    def create_model(self):
        train_ds, val_ds, test_ds = self.create_test_dataset_shuffle()
        class_names = self.create_train_dataset()[1]
        model = tf.keras.Sequential([
            tf.keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
            tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
            tf.keras.layers.MaxPooling2D(2),
            tf.keras.layers.Dropout(.50),
            tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
            tf.keras.layers.MaxPooling2D(2),
            tf.keras.layers.Dropout(.50),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(500, activation='relu'),
            tf.keras.layers.Dropout(.50),
            tf.keras.layers.Dense(num_classes, activation='softmax')
        ])
        model.summary()

        model.compile(
            optimizer='adam',
            loss=tf.losses.SparseCategoricalCrossentropy(),
            metrics=['accuracy'])

        checkpointer = ModelCheckpoint('../save/CNNClassifier.h5', save_best_only=True)
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=5, monitor='val_accuracy',
                                                          restore_best_weights=True)

        history = model.fit(
            train_ds,
            batch_size=batch_size,
            validation_data=val_ds,
            epochs=epochs,
            callbacks=[checkpointer, early_stopping_cb]
        )
        print(history.history)
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']


        epochs_range = range(len(history.history['accuracy']))
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

        model.load_weights('../save/CNNClassifier.h5')
        test_loss, test_acc = model.evaluate(test_ds)

        print("test loss: ", test_loss)
        print()
        print("test accuracy: ", test_acc)

        predictions = model.predict(test_ds)
        score = tf.nn.softmax(predictions[0])

        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )


if __name__ == '__main__':
    FruitsService().hook()