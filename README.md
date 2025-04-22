# Saj Dough Readiness Detection using Raspberry Pi & Machine Learning

This project uses image classification and a camera on a Raspberry Pi to detect whether **Lebanese saj bread dough** is ready (done) or not. The goal is to automate dough readiness detection using machine learning and computer vision.

---

## 📸 Project Overview

A camera connected to a Raspberry Pi takes periodic pictures of the dough. A trained machine learning model classifies the dough as either:

- ✅ **Done**
- ❌ **Not Done**

The project is built in **Python** using **TensorFlow/Keras** and is designed to run efficiently on a Raspberry Pi.

---

## How It Works

1. **Image Collection**
   - Real images of Lebanese saj dough were collected under real-world lighting.
   - Two categories: `done/` and `not_done/`.

2. **Data Augmentation**
   - Techniques: rotation, flip, zoom, brightness changes.
   - Augmented images follow this naming pattern:
     - `aug_dX_Y.jpg` → done dough
     - `aug_ndX_Y.jpg` → not done dough

3. **Dataset Organization**
   - `dataset/train/done` and `dataset/train/not_done` contain original images.
   - `dataset/val/done` and `dataset/val/not_done` contain augmented images.

4. **Model Training**
   - A basic Convolutional Neural Network (CNN) was built using TensorFlow/Keras.
   - Model trained on original images and validated on augmented ones.

5. **Deployment (WIP)**
   - The final model will be deployed on a Raspberry Pi using a camera module.
   - When the dough is ready, the system can trigger a notification or LED.



---

## 🧪 Tech Stack

- **Language**: Python 3
- **Libraries**:
  - `tensorflow`, `keras`
  - `Pillow` (PIL)
  - `numpy`
  - `matplotlib` (optional for plots)
- **Hardware (for deployment)**:
  - Raspberry Pi (any version with camera support)
  - Raspberry Pi Camera Module

---

## 🚀 Future Work

- [ ] Optimize model for Raspberry Pi using TensorFlow Lite
- [ ] Add live camera feed and detection loop
- [ ] Notify user with LED or buzzer when dough is ready

---

## 🙌 Acknowledgments

Special thanks to Lebanese traditions and the iconic **saj bread** that inspired this project.






