import os

def rename_files_based_on_folders(source_dir, target_dir, skip_folder_name="Random"):
    # Get list of folders in the source directory, skipping the "Random" folder
    folders = [f for f in sorted(os.listdir(source_dir)) if os.path.isdir(os.path.join(source_dir, f)) and f != skip_folder_name]

    # Get list of .png files in the target directory
    files = [f for f in sorted(os.listdir(target_dir)) if f.endswith('.png')]

    # Calculate the number of files to rename
    num_files = len(files)
    num_folders = len(folders)

    if num_files > num_folders:
        print("Warning: More files than folders. Some files will not be renamed.")

    # Rename each file to match the folder name with "_icon" appended
    for i, file in enumerate(files):
        if i < num_folders:
            new_name = f"{folders[i]}_icon.png"
        else:
            # If there are more files than folders, keep original names for remaining files
            new_name = file
        old_file_path = os.path.join(target_dir, file)
        new_file_path = os.path.join(target_dir, new_name)
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{file}' to '{new_name}'")

# Example usage
source_dir = 'mysite/static/images/renders'  # Change this to the path of your source directory
target_dir = 'mysite/static/images/icons'  # Change this to the path of your target directory

rename_files_based_on_folders(source_dir, target_dir)
