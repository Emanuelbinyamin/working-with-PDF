
# PDF Watermarking Tool

## Overview

This Python program automates the process of watermarking PDF files.
It's particularly useful for scenarios where you need to protect sensitive documents, such as TV show scripts, from being leaked. 
By watermarking each page of a PDF with a specified watermark, you can identify the source of any unauthorized distribution.

## How It Works

The tool takes a main PDF file (`super.pdf`) and applies a watermark from another PDF file (`wtr.pdf`) to each page. The resulting watermarked PDF is then saved as `watermarked_output.pdf`.

### Key Features
- **Automated Watermarking**: Automatically applies the watermark to all pages of the target PDF, making it ideal for large documents.
- **Leak Prevention**: Useful for industries like entertainment, where scripts or documents need to be protected from leaks. Each script can be watermarked with a unique identifier, such as an actor's name.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Emanuelbinyamin/working-with-PDF.git
    ```
2. **Install the required Python package**:
    ```bash
    pip install PyPDF2
    ```

## Usage

1. **Place your files**:
   - Place the main PDF you want to watermark (`super.pdf`) in the same directory as the script.
   - Place the watermark PDF (`wtr.pdf`) in the same directory as the script.

2. **Run the script**:
    ```bash
    python combinedPdf.py
    ```

3. **Output**:
   - The watermarked PDF will be saved as `watermarked_output.pdf` in the same directory.

## Example Scenario

Imagine you're working on a TV show and need to distribute the script to the cast. To prevent leaks, you can watermark the script with each actor's name. If the script gets leaked, you'll know exactly who was responsible.

## Contributing

Feel free to fork this repository, make changes, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License.
