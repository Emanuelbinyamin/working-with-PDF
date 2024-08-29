
# PDF Rotation Utility 📄🔄

Welcome to the **PDF basic ** project! This Python script allows you to easily rotate pages in a PDF file, and more actions on a pdf file using the PyPDF2 library. 
Whether you're dealing with upside-down pages or just want to adjust the orientation, this tool has you covered.

## Features ✨

- **Rotate PDF Pages**: Rotate individual pages or an entire PDF by any degree.
- **Easy to Use**: Simple command-line interface.
- **Flexible Output**: Save rotated PDFs under a new name to avoid overwriting original files.

## Getting Started 🚀

### Prerequisites

Make sure you have Python installed on your machine. You'll also need to install the `PyPDF2` library:

```bash
pip install PyPDF2
```

### Usage

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Emanuelbinyamin/working-with-PDF/pdf.git
    cd pdf-rotation-utility
    ```

2. Place your PDF file in the `PDFs_here` directory.

3. Run the script to rotate your PDF:

    ```bash
    python pdf.py
    ```

4. The rotated PDF will be saved as `tilt.pdf` in the same directory.

### Example

Here's a quick example of how the script works:

```python
import PyPDF2

with open('PDFs_here/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]

    # Rotate the page by 180 degrees
    rotated_page = page.rotate(180)

    writer = PyPDF2.PdfWriter()
    writer.add_page(rotated_page)

    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
```

## Contributing 🤝

Contributions are welcome! If you have ideas to improve this project, feel free to fork the repository and submit a pull request. You can also open an issue if you encounter any problems.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments 🙌

- Thanks to the [PyPDF2](https://pypi.org/project/PyPDF2/) library for providing the tools to manipulate PDF files.
- Inspired by the need to simplify PDF page rotation for everyday users.

---

Feel free to explore, contribute, and share your thoughts! 😄
```

