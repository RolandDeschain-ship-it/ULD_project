import os

# Function to check if an annotation file is empty
def is_empty_annotation(annotation_file):
    return os.path.getsize(annotation_file) == 0

# Function to remove image and annotation file pair
def remove_empty_annotations(dataset_folder):
    deleted_files = 0
    remaining_images = 0
    deleted_images = []

    # Iterate over train and val directories in images folder
    for dataset_type in ['train', 'val']:
        images_dir = os.path.join(dataset_folder, 'images', dataset_type)
        annotations_dir = os.path.join(dataset_folder, 'annotations', dataset_type)

        for root, _, files in os.walk(images_dir):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    image_file = os.path.join(root, file)
                    annotation_file = os.path.join(annotations_dir, os.path.relpath(root, images_dir), file.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt'))

                    if os.path.exists(annotation_file):
                        if is_empty_annotation(annotation_file):
                            os.remove(image_file)
                            os.remove(annotation_file)
                            deleted_files += 2
                            deleted_images.append(image_file)
                        else:
                            remaining_images += 1
                    else:
                        print("Empty annotation file found:", annotation_file)

    print("Deleted files:", deleted_files)
    print("Remaining images:", remaining_images)
    print("Deleted images:")
    for img in deleted_images:
        print(img)
        
# Example usage
dataset_folder = '/home/benedikt/projects/ULD_project/data/real_1/merged_real_2'
remove_empty_annotations(dataset_folder)
