'''
This script prepares the image generators for training and validation.
It loads the images from dataset/train and dataset/val, rescales the pixel values to the range [0, 1], resizes all images to 224x224 pixels, and batches them into groups of 32 images.
The output (train_generator and val_generator) is then used to feed data into the model during training.

'''
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_dir = 'dataset/train'
val_dir = 'dataset/val'


img_height, img_width = 224, 224
batch_size = 32


train_datagen = ImageDataGenerator(
    rescale=1./255,
)

val_datagen = ImageDataGenerator(
    rescale=1./255,
)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary'  # 2 classes: done or not_done
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary'
)
