'''
This script applies data augmentation (rotation, zoom, brightness, flip, etc.) to images in the images/ folder using TensorFlow’s ImageDataGenerator,
generating 3 new images per original and saving them in the augmented/ folder.

'''

import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img, array_to_img
import numpy as np


input_folder = 'images'
output_folder = 'augmented'
os.makedirs(output_folder, exist_ok=True)

#augmentation parameters
datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    brightness_range=[0.8, 1.2],
    shear_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)


augmented_per_image = 3

# Loop through all images in the dataset
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".PNG") or filename.endswith(".jfif") :
        img_path = os.path.join(input_folder, filename)
        img = load_img(img_path)  
        x = img_to_array(img)     
        x = np.expand_dims(x, axis=0)  # Add batch dimension

    
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir=output_folder,
                                  save_prefix='aug_' + filename.split('.')[0],
                                  save_format='jpg'):
            i += 1
            if i >= augmented_per_image:
                break
print("Done! Augmented images saved in 'augmented/' folder.")