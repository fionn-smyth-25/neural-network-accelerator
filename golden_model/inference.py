# as opposed to training, which we ideally only do once
# inference is done each time we actually want to use the model we just trained

from tensorflow import keras
from tensorflow.keras.datasets import mnist
import numpy as np
import matplotlib as plt
from PIL import Image
import numpy as np

# prediction function

def predict(image):
    image = np.expand_dims(image, axis = 0) # turns (28, 28) into (1, 28, 28) because keras expects a batch of images
    prediction = model.predict(image, verbose = 0) # output has shape (1, 10)
    return np.argmax(prediction), prediction[0] # we return prediciton[0] again because keras expects a batch even if we only send one image

# load the model

model = keras.models.load_model("model.keras")

# load an image
# we need to do some preprocessing in order for an image to be suitable with a mnist model
# must be resized to 28x28 pixels, and the image must be greyscale

image = Image.open("input_images/my_digit.png").convert("L") # load image, convert to greyscale
image = image.resize((28,28)) # resize
image = np.array(image) # creates an array based on our image

# predict

digit, probs = predict(image)

print(digit)
