import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import load_model

# Load the trained model
model = load_model("saved_models/Handwritten_digits.keras")

def test_try():
    image_num = 1
    while os.path.isfile(f"user_images/test{image_num}.png"):
        try:
            img = cv2.imread(f"user_images/test{image_num}.png")[:, :, 0]
            img_array = np.invert(np.array(img).reshape(1, 28, 28, 1))
            prediction = model.predict(img_array)
            prediction = np.argmax(prediction)
            print(f"Prediction for test{image_num}.png: {prediction}")
            plt.imshow(img_array[0], cmap=plt.cm.binary)
            plt.show()
        except Exception as e:
            print(f"Error processing test{image_num}.png: {e}")
        finally:
            image_num += 1

# Call the function to test predictions
test_try()
