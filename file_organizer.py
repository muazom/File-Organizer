import os
import shutil

# Change this to the folder you want to organize
DOWNLOADS_FOLDER = r"C:\Users\YourUsername\Downloads"

# Define the folders for each file type
FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}

# Make sure all folders exist
for folder in FOLDERS:
    folder_path = os.path.join(DOWNLOADS_FOLDER, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to corresponding folders
for file in os.listdir(DOWNLOADS_FOLDER):
    file_path = os.path.join(DOWNLOADS_FOLDER, file)
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in FOLDERS.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(DOWNLOADS_FOLDER, folder, file))
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(DOWNLOADS_FOLDER, "Others", file))

print("Files have been organized successfully!")
