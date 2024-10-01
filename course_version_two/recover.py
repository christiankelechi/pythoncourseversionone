import os
import shutil

def recover_files(source_folder, recovery_folder):
    """
    Scans the source folder and copies all files to the recovery folder.
    
    Parameters:
    - source_folder (str): The path to the folder to scan for files.
    - recovery_folder (str): The path to the folder where recovered files will be copied.
    """
    # Create the recovery folder if it does not exist
    if not os.path.exists(recovery_folder):
        os.makedirs(recovery_folder)

    # Loop through all files in the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file_path = os.path.join(root, file)
            # Create the destination path
            destination_file_path = os.path.join(recovery_folder, file)
            # Copy the file to the recovery folder
            try:
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Recovered: {source_file_path} -> {destination_file_path}")
            except Exception as e:
                print(f"Failed to recover {source_file_path}: {e}")

# Example usage
source_folder = 'F:\\'  # Change this to your source folder path
recovery_folder = 'c:\\'  # Change this to your recovery folder path

recover_files(source_folder, recovery_folder)
