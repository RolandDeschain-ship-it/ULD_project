import os
import shutil
import random


# List of paths to the datasets
dataset_paths = [
    '/home/benedikt/projects/ULD_project/data/real_1/merged_real_2',
    '/home/benedikt/projects/ULD_project/data/undamaged/combined',
    ]

# Combined output folder
combined_output_folder = '/home/benedikt/projects/ULD_project/data/combined/combined_5'

# Function to copy images and annotations from each dataset
# Function to copy images and annotations from each dataset
def copy_data(source_folder, destination_folder):
    # Ensure destination directories exist
    os.makedirs(destination_folder, exist_ok=True)

    # List all files in the source folder
    files = os.listdir(source_folder)

    # Copy files to corresponding combined folder
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.copy(source_path, destination_path)

# Initialize counts for images and annotations
train_image_count = 0
val_image_count = 0
train_annotation_count = 0
val_annotation_count = 0

# Iterate over each dataset
for dataset_path in dataset_paths:
    # Copy train images and annotations
    copy_data(os.path.join(dataset_path, 'images', 'train'), os.path.join(combined_output_folder, 'images', 'train'))
    copy_data(os.path.join(dataset_path, 'labels', 'train'), os.path.join(combined_output_folder, 'labels', 'train'))

    # Copy validation images and annotations
    copy_data(os.path.join(dataset_path, 'images', 'val'), os.path.join(combined_output_folder, 'images', 'val'))
    copy_data(os.path.join(dataset_path, 'labels', 'val'), os.path.join(combined_output_folder, 'labels', 'val'))

    # Update counts
    train_image_count += len(os.listdir(os.path.join(dataset_path, 'images', 'train')))
    val_image_count += len(os.listdir(os.path.join(dataset_path, 'images', 'val')))
    train_annotation_count += len(os.listdir(os.path.join(dataset_path, 'labels', 'train')))
    val_annotation_count += len(os.listdir(os.path.join(dataset_path, 'labels', 'val')))

# Output counts
print("Train images:", train_image_count)
print("Validation images:", val_image_count)
print("Train labels:", train_annotation_count)
print("Validation labels:", val_annotation_count)
