# `pyneverduplex`

`pyneverduplex` is a Python script that merges two PDF files into a single PDF document. It is designed to merge PDF files that represent the front pages and back pages (reversed) of a stack of double-sided documents fed into a non-duplex scanner, compensating for the lack of duplexness and interleaving the pages into the correct order.

> back pages are reversed because when feeding the scanner it's easier to just flip the entire stack around to the back pages 🔁 instead of flipping each individual page to preserve the order

## Prerequisites

- Python 3.x installed on your system.

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine using:

```bash
git clone git@github.com:json2d/pyneverduplex
```

### Step 2: Navigate to the Project Directory

Change into the project directory:

```bash
cd pyneverduplex
```

### Step 3: Set Up a Virtual Environment (Optional)

It is recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment using the following commands:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 4: Install Required Packages

Install the required Python packages using `pip` and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

### Step 5: Place Your PDF Files

Ensure you have your PDF files ready. The script expects two files:

- `tmp/front_pages.pdf`: The PDF containing the front pages of the documents.
- `tmp/back_pages.pdf`: The PDF containing the back pages of the documents.

Place these files in the same directory as the script, or update the paths in the script if they are located elsewhere.

### Step 6: Run the Script

Execute the script to merge the PDF files:

```bash
python merge_pdfs.py tmp/front_pages.pdf tmp/back_pages_reversed.pdf tmp/merged_document.pdf
```

The script will output a new PDF file named `tmp/merged_document.pdf` with the pages interleaved correctly.

## Notes

- The script assumes both PDF files have the same number of pages. Ensure that the front and back PDF files match in page count.
- Modify the paths in the script if your files are located in different directories.
- Heavy lift by ChatGPT 4o
  - https://chatgpt.com/share/e193d449-6e4d-4db6-b6de-c6c0518a585a

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
