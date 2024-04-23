import os
import shutil
import random

# Path to the folder containing images and annotations
data_folder = "/home/benedikt/projects/ULD_project/data/class_test/alu/alu_real_ext (copy)/all"

# Path to the output folders
output_folder = "/home/benedikt/projects/ULD_project/data/class_test/alu/alu_real_ext"

# Percentage of data to be used for validation
validation_split = 0.2

# Create train and validation folders for images
os.makedirs(os.path.join(output_folder, 'images', 'train'), exist_ok=True)
os.makedirs(os.path.join(output_folder, 'images', 'val'), exist_ok=True)

# Create train and validation folders for annotations
os.makedirs(os.path.join(output_folder, 'labels', 'train'), exist_ok=True)
os.makedirs(os.path.join(output_folder, 'labels', 'val'), exist_ok=True)

# List all image files in the data folder
image_files = [file for file in os.listdir(data_folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Shuffle the list of image files
random.shuffle(image_files)

# Calculate the split index
split_index = int(len(image_files) * validation_split)

# Split files into train and validation sets
train_image_files = image_files[split_index:]
val_image_files = image_files[:split_index]

print("Number of train images:", len(train_image_files))
print("Number of validation images:", len(val_image_files))

# Copy images to corresponding train and validation folders
for file in train_image_files:
    source_path = os.path.join(data_folder, file)
    destination_path = os.path.join(output_folder, 'images', 'train', file)
    print("Copying", source_path, "to", destination_path)
    shutil.copy(source_path, destination_path)

for file in val_image_files:
    source_path = os.path.join(data_folder, file)
    destination_path = os.path.join(output_folder, 'images', 'val', file)
    print("Copying", source_path, "to", destination_path)
    shutil.copy(source_path, destination_path)

# Function to copy annotations based on image files already copied
def copy_annotations(image_files, source_folder, destination_folder):
    for file in image_files:
        filename, _ = os.path.splitext(file)
        annotation_file = filename + '.txt'
        source_path = os.path.join(source_folder, annotation_file)
        destination_path = os.path.join(destination_folder, annotation_file)
        if os.path.exists(source_path):
            print("Copying", source_path, "to", destination_path)
            shutil.copy(source_path, destination_path)

# Copy annotations to corresponding train and validation folders
copy_annotations(train_image_files, data_folder, os.path.join(output_folder, 'labes', 'train'))
copy_annotations(val_image_files, data_folder, os.path.join(output_folder, 'labels', 'val'))
