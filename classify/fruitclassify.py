'''
Filename: fruitclassify.py
Path: /GitHub/hackathon-WIT
Created Date: Tuesday, June 15th 2021, 2:02:43 am
Author: Ravi Shekhar Singh

Copyright (c) 2021 
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
import os
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from sklearn.preprocessing import LabelEncoder


sample_size = 200
width = 50
height = 50

files = []

adress = "/Users/rootsr/Documents/Dataset/fruits-360/Training/{}"
os.chdir("/Users/rootsr/Documents/Dataset/fruits-360/Training/")
for i in os.listdir(os.getcwd()):
    files.append(i)

data = {}
for f in files:
    data[f]=[]
for col in files:
    os.chdir(adress.format(col))
    for i in os.listdir(os.getcwd()):
        if i.endswith('.jpg'):
            data[col].append(i)

start = time.time()
image_data = []
image_target = []

for title in files:
    os.chdir(adress.format(title))
    counter = 0
    for i in data[title]:
        img = cv2.imread(i)
        image_data.append(cv2.resize(img,(width, height)))
        image_target.append(title)
        counter += 1
        if counter == sample_size:
            break
    print("Compiled Class",title)
calculate_time = time.time() - start    
print("Calculate Time",round(calculate_time,5))

start = time.time()
image_data_test = []
image_target_test = []

for title in files:
    os.chdir(adress.format(title))
    sayac = 0
    for i in data[title][sample_size:]:
        img = cv2.imread(i)
        image_data_test.append(cv2.resize(img,(width, height)))
        image_target_test.append(title)
        sayac += 1
        if sayac == 50:
            break
    print("Compiled Class",title)
calculate_time = time.time() - start    
print("Calculate Time",round(calculate_time,5))


image_data = np.array(image_data)
size = image_data.shape[0]
image_data.shape


image_data_test = np.array(image_data_test)
size = image_data_test.shape[0]
image_data_test.shape


labels = LabelEncoder()
labels.fit(image_target)

train_images = image_data / 255.0
train_labels = labels.transform(image_target)
test_images = image_data_test / 255.0
test_labels = labels.transform(image_target_test)
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(width,height,3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(131))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=8, 
                    validation_data=(test_images, test_labels))

# Display the model's architecture
print(model.summary())
model.save_weights("fruits.h5")

plt.style.use('ggplot')
plt.figure(figsize=(10, 5))
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

def Prediction(image):
    
    global width, height, files, labels
    
    img = cv2.resize(image,(width,height))
    
    test = img / 255.0
    
    pred = model.predict(np.array([image])).argmax()
    
    return labels.inverse_transform([pred])[0]

plt.figure(figsize=(15,15))
for i in range(1,17):
    fig = np.random.choice(np.arange(1,size+1))
    plt.subplot(4,4,i)
    plt.imshow(image_data[fig], cmap="gray", origin='upper', interpolation = 'bicubic')
    plt.title(image_target[fig])
    plt.ylabel("| Pred:{} |".format(Prediction(image_data[fig])),fontsize=17)
    plt.xticks([]), plt.yticks([])
plt.show()
