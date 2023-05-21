from tensorflow import keras
from PIL import Image
import numpy as np

model = keras.models.load_model("garbage_84_79.h5")
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

data = "example_clothes.jpg"
dataPath = "C:/Users/peter/PycharmProjects/ITP 259/DavisHackathon/" + data

image = Image.open(data)
resized_image = image.resize((224, 224))
image_array = np.array(resized_image)
if image_array.shape[2] != 3:
    image_array = image_array[:, :, :3]
image_array = np.expand_dims(image_array, axis=0)
image_array = image_array.astype(np.float32) / 255.0

pred = model.predict(image_array)
pred_classes = np.argmax(pred, axis=1)
#print(pred_classes)
dict = {0:"Battery", 1:"Compost", 2:"Clothes", 3:"Recycle", 4:"Trash"}
print("The predicted object is: ", dict[pred_classes[0]])
#print(predictions)


