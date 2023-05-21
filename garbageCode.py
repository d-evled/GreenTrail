import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import glob
from tqdm import tqdm
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.preprocessing.image import ImageDataGenerator

# The folders containing the train and test images

train_path = "path/to/train/directory"
test_path = "path/to/test/directory"

# Initiate lists to separate data
# X_train = []
# y_train = []
# X_test = []
# y_test = []

# Load data from folders into test and train lists
# categories = ["O", "R"]
# for folder in glob.glob(train_path + "/*"):
#     for file in tqdm(glob.glob(folder + "/*")):
#         image = cv2.imread(file)
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image = cv2.resize(image, (224, 224))  # Resize the image to the desired size
#         X_train.append(image)
#         y_train.append(categories.index(folder[-1]))
#
# for folder in glob.glob(test_path + "/*"):
#     for file in tqdm(glob.glob(folder + "/*")):
#         image = cv2.imread(file)
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         image = cv2.resize(image, (224, 224))  # Resize the image to the desired size
#         X_test.append(image)
#         y_test.append(categories.index(folder[-1]))

# Looks at first 30 images and plots them
# for i in range(30):
#     plt.subplot(5, 6, i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(X_train[i])
#     plt.xlabel(y_train[i])
# plt.show()

# Build the CNN model
model = Sequential()
model.add(Conv2D(100, kernel_size=(10,10), strides=(5,5), padding="same", activation="relu", input_shape=(224, 224, 3)))
model.add(Conv2D(50, kernel_size=(10,10), strides=(3,3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(200, kernel_size=(3,3), strides=(1,1), padding="same", activation="relu"))

model.add(Flatten())
model.add(Dense(50, activation="relu"))
model.add(Dropout(0.4))
model.add(Dense(20, activation="relu"))
model.add(Dropout(0.3))

model.add(Dense(5, activation="softmax"))

# Display model summary and number of parameters
model.summary()

# Scale pixel values by 255 for faster training
train_gen = ImageDataGenerator(rescale = 1./255)
test_gen = ImageDataGenerator(rescale = 1./255)

# Set the parameters for routing the images
batch_size = 50

train_generator = train_gen.flow_from_directory(train_path, target_size= (224,224),
                                                batch_size = batch_size, color_mode= "rgb",class_mode= "categorical")

test_generator = test_gen.flow_from_directory(test_path, target_size= (224,224),
                                              batch_size = batch_size, color_mode= "rgb", class_mode= "categorical")

# Compile the model
model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam")

# Train the model
h = model.fit_generator(generator=train_generator, epochs=20, validation_data=test_generator, verbose=True)

# 9. Plot the loss and accuracy curves for both train and validation sets.
# Loss
# plt.plot(h.history["loss"], "black", linewidth=2.0)
# plt.plot(h.history["val_loss"], "green", linewidth=2.0)
# plt.legend(["Training Loss", "Validation Loss"], fontsize=14)
# plt.xlabel("Epochs", fontsize=10)
# plt.ylabel("Loss", fontsize=10)
# plt.title("Loss Curves", fontsize=12)
# plt.show()
#
# # Accuracy
# plt.plot(h.history["accuracy"], "black", linewidth=2.0)
# plt.plot(h.history["val_accuracy"], "green", linewidth=2.0)
# plt.legend(["Training Accuracy", "Validation Accuracy"], fontsize=14)
# plt.xlabel("Epochs", fontsize=10)
# plt.ylabel("Accuracy", fontsize=10)
# plt.title("Accuracy Curves", fontsize=12)
# plt.show()

save_path = "path/to/saved model/directory"
model.save(save_path + "garbage.h5")
