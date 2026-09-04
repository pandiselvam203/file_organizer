import os
import shutil

folder = input("Enter folder path: ")

folders = {
    ".txt": "text",
    ".pdf": "pdfs",
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".doc": "documents",
    ".docx": "documents",
    ".mp3": "music",
    ".wav": "music",
    ".mp4": "videos",
    ".mkv": "videos"
}

files = os.listdir(folder)

for file in files:

    file_path = os.path.join(folder, file)

    if not os.path.isfile(file_path):
        continue

    name, extension = os.path.splitext(file)

    extension = extension.lower()

    if extension in folders:

        destination = folders[extension]

    else:

        destination = "another files"

    destination_folder = os.path.join(folder, destination)

    os.makedirs(destination_folder, exist_ok=True)

    shutil.move(
        file_path,
        os.path.join(destination_folder, file)
    )

    print(file, "→", destination)
