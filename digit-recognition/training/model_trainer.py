import keras
from keras.src.models import Sequential
from keras.src.losses import CategoricalCrossentropy
from keras.src.layers import Flatten, Dense, Conv2D, MaxPooling2D
import numpy as np

# Load and normalize MNIST data
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

x_train = np.array(x_train).reshape(-1, 28, 28, 1)
x_test = np.array(x_test).reshape(-1, 28, 28, 1)

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# Build the model
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

# Compile the model
model.compile(optimizer="Adam", loss=CategoricalCrossentropy(from_logits=False), metrics=["accuracy"])

# Train the model
model.fit(x_train, y_train, epochs=50, validation_data=(x_test, y_test))

# Save the trained model
model.save("../saved_models/Handwritten_digits.keras")
