# JPNtoPNGconverter
The JPNtoPNGconverter is a Python script that converts JPG files to PNG format. It takes command-line arguments to specify the input and output folders.

Here's how the program works:

It first checks the number of command-line arguments. If there are more than three arguments, it prints an error message and exits. If there are fewer than two arguments, it also prints an error message and exits.

The input folder is assigned to the variable input_folder, which is the first command-line argument provided. If the input folder does not exist, an error message is printed, and the program exits. Otherwise, the path of the input folder is displayed.

If a second folder is provided as a command-line argument, it is assigned to the variable output_folder. If the output folder does not exist, a new folder with the provided name is created. The path of the output folder is then displayed.

If only one folder is provided as a command-line argument, a default output folder named "NewFolder" is created if it doesn't already exist. The path of the output folder is displayed.

The program loops through the files in the input folder. If a file has the ".jpg" extension, it opens the image using the PIL library. The file extension is then changed to ".png" by using the os.path.splitext() function, and the image is saved in the output folder with the new file name.

To run the program in the terminal, the command should be: python3 JPGtoPNGconverter.py <input_folder> <output_folder>

Please note that the program assumes that the necessary Python libraries (sys, os, and PIL) are installed before running it.
