import os
import shutil

# Base directory
base_dir = r'C:\Users\User\OneDrive - University of Balamand\Desktop\MMM'
augmented_dir = os.path.join(base_dir, 'cleaned')
val_dir = os.path.join(base_dir, 'dataset', 'val')

# Make sure the val subdirectories exist
for cls in ['done', 'not_done']:
    os.makedirs(os.path.join(val_dir, cls), exist_ok=True)

# Go through each image and move it to the appropriate class
for fname in os.listdir(augmented_dir):
    fname_lower = fname.lower()
    src_path = os.path.join(augmented_dir, fname)

    if fname_lower.startswith("aug_d"):
        dst_path = os.path.join(val_dir, 'done', fname)
    elif fname_lower.startswith("aug_nd"):
        dst_path = os.path.join(val_dir, 'not_done', fname)
    else:
        print(f"⚠️ Skipping file (unknown label): {fname}")
        continue

    shutil.copy(src_path, dst_path)

print("✅ Augmented images sorted into 'val/done' and 'val/not_done' based on filenames.")
