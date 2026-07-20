# as opposed to training, which we ideally only do once
# inference is done each time we actually want to use the model we just trained

import tensorflow as tf
import numpy as np
from PIL import Image

# load the model

model = tf.keras.models.load_model("model.keras")

# prediction function

def predict(image_path):

    # load an image
    # we need to do some preprocessing in order for an image to be suitable with a mnist model
    # must be resized to 28x28 pixels, and the image must be greyscale

    # convert to greyscale
    img = Image.open(image_path).convert("L")

    # resize
    img = img.resize((28,28)) 

    # create array based on our image
    img = np.array(img)

    # turns (28, 28) into (1, 28, 28) because keras expects a batch of images
    img = np.expand_dims(img, axis = 0)

    # add channel dimension
    img = np.expand_dims(img, axis=-1)
    
    # debug
    print(img.shape)

    prediction = model.predict(img, verbose = 0)

    digit = np.argmax(prediction)

    confidence = np.max(prediction)

    return digit, confidence
