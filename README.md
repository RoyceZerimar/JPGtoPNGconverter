# JPG to PNG Converter

## Overview

This Python script converts images in JPG format to PNG format. It provides a command-line interface for specifying input and output folders.

### Usage

To use the JPG to PNG Converter, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your_username/jpg-to-png-converter.git
```

2. Navigate to the project directory:

```bash
cd jpg-to-png-converter
```

3. Run the script:

```bash
python JPGtoPNGconverter.py input_folder [output_folder]
```

Replace `input_folder` with the path to the folder containing JPG images you want to convert. Optionally, you can specify `output_folder` as the destination folder for the converted PNG images. If `output_folder` is not provided, a new folder named "NewFolder" will be created in the current directory to store the converted images.

### Example

Convert JPG images in a folder named "Pokedex" to PNG format and save them in a folder named "ImageFolder":

```bash
python JPGtoPNGconverter.py Pokedex ImageFolder
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
