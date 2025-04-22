'''
This script reads images from the augmented/ folder, crops the top 15% to remove camera distortion,
resizes them to 224×224 pixels, normalizes them, and saves the cleaned images in the cleaned/ folder.
'''

import cv2
import os
import numpy as np


input_dir = 'augmented'
output_dir = 'cleaned'
os.makedirs(output_dir, exist_ok=True)


target_size = (224, 224)

# Loop through all images
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f" Skipping unreadable file: {filename}")
            continue

        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Crop top 15% to remove distortion
        h, w = img.shape[:2]
        crop_top = int(h * 0.15)
        img_cropped = img[crop_top:, :]

        
        img_resized = cv2.resize(img_cropped, target_size)

        # Normalize to [0,1] and convert back to uint8 for saving
        img_normalized = img_resized.astype('float32') / 255.0
        img_save = (img_normalized * 255).astype('uint8')

       
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, cv2.cvtColor(img_save, cv2.COLOR_RGB2BGR))

print(" Done! Cleaned images saved in 'cleaned/' folder.")
