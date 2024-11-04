import os
import shutil

def organize_downloads():
    downloads_folder = "C:\\Users\\YNR\\Downloads"  

    # Define a dictionary to map file extensions to their respective folder names
    extension_to_folder = {
        ".jpg": "Downloads Images",
        ".exe": "Downloads Applications",
        ".png": "Downloads Images",
        ".jpeg": "Downloads Images",
        ".gif": "Downloads Images",
        ".pdf": "Downloads PDFs",
        ".docx": "Downloads Documents",
        ".txt": "Downloads Text",
        # Add more extensions and folder names as needed
    }

    # Create the destination folders if they don't exist
    for folder_name in extension_to_folder.values():
        folder_path = os.path.join(downloads_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate through each file in the Downloads folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Check if the file is a file (not a directory)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            # Check if the file extension is in the dictionary
            if file_extension in extension_to_folder:
                destination_folder = extension_to_folder[file_extension]
                destination_path = os.path.join(downloads_folder, destination_folder, filename)

                # Move the file to the appropriate destination folder
                shutil.move(file_path, destination_path)

if __name__ == "__main__":
    organize_downloads()