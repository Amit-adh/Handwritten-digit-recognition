import os
import keras
import numpy as np
import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Load the trained model
model = keras.models.load_model("./saved_models/Handwritten_digits.keras")


class DrawApp:
    def __init__(self, root):
        self.brush = 4
        self.root = root
        self.root.title("Handwritten Digit Recognition")

        self.canvas_height = 360
        self.canvas_width = 500
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="gray")
        self.canvas.create_rectangle((10, 20, 290, 300), fill="white")
        self.canvas.pack()

        self.canvas.create_window((90, 320), window=ttk.Button(self.canvas, text="Check", command=self.predict))
        self.canvas.create_window((210, 320), window=ttk.Button(self.canvas, text="Clear", command=self.clear_canvas))

        self.image = Image.new("L", (self.canvas_width, self.canvas_height), 255)
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<MouseWheel>", self.adjust_brush)

    def paint(self, event):
        x, y = event.x, event.y
        if 10 + self.brush / 3 <= x <= 290 - self.brush / 3 and 30 + self.brush / 3 <= y <= 310 - self.brush / 3:
            self.canvas.create_oval((x - self.brush / 2, y - self.brush / 2,
                                     x + self.brush / 2, y + self.brush / 2), fill="black", tags="drawing")
            self.draw.ellipse((x - self.brush / 2, y - self.brush / 2,
                               x + self.brush / 2, y + self.brush / 2), fill=0)

    def adjust_brush(self, event):
        if event.delta > 0 and self.brush < 16:
            self.brush += 1
        elif event.delta < 0 and self.brush > 1:
            self.brush -= 1

    def clear_canvas(self):
        self.canvas.delete("drawing")
        self.canvas.delete("prediction")
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), 255)
        self.draw = ImageDraw.Draw(self.image)

    def predict(self):
        cropped_img = self.image.crop((10, 20, 290, 300)).resize((28, 28))
        img_array = np.invert(np.array(cropped_img))
        img_array = img_array / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        prediction = np.argmax(model.predict(img_array))
        self.canvas.create_window((400, 150), tags="prediction", window=ttk.Label(
            self.canvas, background="white", font=("Arial", 16), text=f"Prediction: {prediction}"))

        # Optional visualization
        # plt.imshow(img_array[0], cmap=plt.cm.binary)
        # plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawApp(root)
    root.mainloop()
