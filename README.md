# 🧠 Handwritten Digit Recognition with CNN and Tkinter

This project is a simple handwritten digit recognition system built using a Convolutional Neural Network (CNN) in Keras and a graphical drawing interface in Tkinter. The user can draw digits (0–9) on the canvas, and the model will predict what digit has been drawn.

---

## 🚀 Features

- Trainable CNN model on the MNIST dataset
- Drawing interface built using Tkinter
- Real-time digit prediction from the canvas
- Option to test saved images (`test1.png`, `test2.png`, etc.)
- Adjustable brush size for better drawing control

---

## 🖥️ Interface Preview

The canvas includes:
- A white box to draw digits
- "Check" button to predict the digit
- "Clear" button to reset the canvas

---

## 🧠 Model Architecture

The CNN model uses:

- 2 convolutional layers (`Conv2D`)
- 2 max pooling layers (`MaxPooling2D`)
- Fully connected layers (`Dense`)
- Final softmax layer for digit classification

---

## 📁 File Structure

```bash
.
├── model/
│   └── model_trainer.py        # Script to train and save the model
├── digit_gui.py                # Main GUI app for drawing and prediction
├── Handwritten_digits.keras    # Trained model file
├── user_images/
│   └── test1.png               # Sample test images (optional)
└── README.md
# 🧠 Handwritten Digit Recognition with CNN and Tkinter

This project is a simple handwritten digit recognition system built using a Convolutional Neural Network (CNN) in Keras and a graphical drawing interface in Tkinter. The user can draw digits (0–9) on the canvas, and the model will predict what digit has been drawn.

---

## 🚀 Features

- Trainable CNN model on the MNIST dataset
- Drawing interface built using Tkinter
- Real-time digit prediction from the canvas
- Option to test saved images (`test1.png`, `test2.png`, etc.)
- Adjustable brush size for better drawing control

---

## 🖥️ Interface Preview

The canvas includes:
- A white box to draw digits
- "Check" button to predict the digit
- "Clear" button to reset the canvas

---

## 🧠 Model Architecture

The CNN model uses:

- 2 convolutional layers (`Conv2D`)
- 2 max pooling layers (`MaxPooling2D`)
- Fully connected layers (`Dense`)
- Final softmax layer for digit classification

---

## 📁 File Structure

```bash
.
├── model/
│   └── model_trainer.py        # Script to train and save the model
├── digit_gui.py                # Main GUI app for drawing and prediction
├── Handwritten_digits.keras    # Trained model file
├── user_images/
│   └── test1.png               # Sample test images (optional)
└── README.md
