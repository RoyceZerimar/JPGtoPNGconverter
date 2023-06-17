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
    output_folder = sys.argv[2]
    # 2 check if second folder exist if not creat the folder
    if not os.path.isdir(output_folder):
        print(f"creating new folder: {output_folder}")
        os.makedirs(output_folder)
    print(f"output_folder: {output_folder}")


elif len(sys.argv) == 2:  # creating a new folder if a second folder is not provided
    output_folder = "NewFolder"
    if not os.path.isdir(output_folder):
        print(f"Creating new folder: {output_folder}")
        os.makedirs(output_folder)
    print(f"output_folder: {output_folder}")


# 3 loop through fist folder then convert to png and add them to the new folder

for file_name in os.listdir(input_folder):
    if file_name.endswith(".jpg"):
        image = Image.open(os.path.join(input_folder, file_name))

        new_filename = os.path.splitext(file_name)[0] + '.png'
        image.save(os.path.join(output_folder, new_filename))

#  python3 JPGtoPNGconverter.py Pokedex
