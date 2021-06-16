'''
Filename: fruit_transfer_learning.py
Path: /GitHub/hackathon-WIT
Created Date: Tuesday, June 14th 2021, 9:34:12 pm
Author: Ravi Shekhar Singh

Copyright (c) 2021 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator,img_to_array,load_img
from keras.layers import Dense
from keras.models import Sequential
from keras.applications.vgg16 import VGG16
from glob import glob

# define train and test data path
train_path = "/Users/rootsr/Documents/Dataset/fruits-360/Training/"
test_path = "/Users/rootsr/Documents/Dataset/fruits-360/Test/"

img = load_img(train_path + "Avocado/0_100.jpg")

plt.imshow(img)
plt.show();

x = img_to_array(img)
print(x.shape)

numberOfClass = len(glob(train_path + "/*"))
print(numberOfClass)

vgg = VGG16()
print(vgg.summary())

vgg_layer_list = vgg.layers
print(len(vgg_layer_list))

vgg_layer_list[-1]

model = Sequential()
for i in range(len(vgg_layer_list)-1):
    model.add(vgg_layer_list[i])

print(model.summary())

for layers in model.layers:
    layers.trainable = False

model.add(Dense(numberOfClass,activation="softmax"))

print(model.summary())

model.compile(loss="categorical_crossentropy",
             optimizer="rmsprop",
             metrics=["accuracy"])

train_data = ImageDataGenerator().flow_from_directory(train_path,target_size=(224,224))

test_data = ImageDataGenerator().flow_from_directory(test_path,target_size=(224,224))

batch_size=64

hist = model.fit_generator(train_data,
                           steps_per_epoch=1600//batch_size,
                           epochs=10,
                           validation_data=test_data,
                           validation_steps=800//batch_size)

model.save_weights("fruits_model.h5")

print(hist.history.keys())

plt.plot(hist.history["loss"],label="training loss")
plt.plot(hist.history["val_loss"],label="validation loss")
plt.legend()
plt.show();

plt.plot(hist.history["accuracy"],label="training accuracy")
plt.plot(hist.history["val_accuracy"],label="validation accuracy")
plt.legend()
plt.show();

