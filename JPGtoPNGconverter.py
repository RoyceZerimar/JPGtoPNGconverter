import sys
import os
from PIL import Image

# 1grab the first and second file

if len(sys.argv) > 3:
    print("Please provide no more than two folders as command-line arguments")
    sys.exit(1)

elif len(sys.argv) < 2:
    print("Please provide at least one folder as a command-line argument")
    sys.exit(1)

# checking to see if input_folder exist
input_folder = sys.argv[1]
if not os.path.isdir(input_folder):
    print(f"folder 1 does not exist: {input_folder}")
    sys.exit(1)
print(f'input_folder: {input_folder}')

# checking to see if the user provided a second folder
if len(sys.argv) == 3:
    folder2 = sys.argv[2]
    # 2 check if second folder exist if not creat the folder
    if not os.path.isdir(folder2):
        print(f"creating new folder: {folder2}")
        os.makedirs(folder2)
    print(f"Folder2: {folder2}")


elif len(sys.argv) == 2:  # creating a new folder if a second folder is not provided
    folder2 = "NewFolder"
    if not os.path.isdir(folder2):
        print(f"Creating new folder: {folder2}")
        os.makedirs(folder2)
    print(f"Folder2: {folder2}")


# 3 loop through fist folder then convert to png and add them to the new folder

for file_name in os.listdir(input_folder):
    if file_name.endswith(".jpg"):
        image_path = os.path.join(input_folder, file_name)

        img = Image.open(image_path)
        img.show()
        break
#  python3 JPGtoPNGconverter.py Pokedex
