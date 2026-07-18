# for recognising digits, we can use the MNIST database
# the following is from wikipedia for MNIST:
# The MNIST database (Modified National Institute of Standards and Technology database) 
# is a large database of handwritten digits that is commonly used for training various image processing systems.
# The MNIST database contains 60,000 training images and 10,000 testing images.
# They were all normalized to fit into 28 x 28 pixels

from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# we will use the following neural network 
# 784 inputs (28x28) -> 64 neurons -> 10 outputs (10 digits)
# the neural network is dense because each node in a layer connects to each node in the next layer
# a neuron consists of a linear function followed by a non-linear function (called the activation function)
# for our layers, the activation function is always relu (outputs the input only if greater than zero, otherwise outputs zero)
# the activation function for the output layer is softmax,
# which converts a vector of real numbers into a probability distributiona
# we can then choose the highest probabilty output as the output digit based on our input image (im guessing?)

from tensorflow import keras

model = keras.Sequential([
        keras.layers.Flatten(input_shape = (28, 28)),
        keras.layers.Dense(64, activation = "relu"),
        keras.layers.Dense(10, activation = "softmax")
    ])

# train the model

model.compile(
    optimizer = "adam",
    loss = "sparse_categorical_crossentropy",
    metrics = ["accuracy"]
)

model.fit(x_train, y_train, epochs = 10)

# export weights

weights = model.get_weights() # get weights
fixed = (weights[0] * 256).astype(int) # convert to fixed point (for FPGA usage later)

with open("weights.mem","w") as f:
    for value in fixed.flatten():
        f.write(f"{value & 0xFFFF:04X}\n")

# verification

predictions = model.predict(x_test)

predicted = predictions.argmax(axis = 1)

accuracy = (predicted == y_test).mean()

print(f"Accuracy = {accuracy*100:.2f}%")

# inspect individual examples

import matplotlib.pyplot as plt

i = 42

plt.imshow(x_test[i], cmap = "gray")
plt.savefig("example.png") 
plt.close()

print("Prediction:", predicted[i])
print("Actual:", y_test[i])
