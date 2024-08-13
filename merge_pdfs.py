import argparse
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(front_pages_path, back_pages_reversed_path, output_path):
    # Create PDF readers for the front and back pages
    front_reader = PdfReader(front_pages_path)
    back_reader = PdfReader(back_pages_reversed_path)
    
    # Verify both PDFs have the same number of pages
    if len(front_reader.pages) != len(back_reader.pages):
        print("Error: The number of pages in the front and back PDF files do not match.")
        return

    # Create a PDF writer to write the merged document
    writer = PdfWriter()

    # Unreverse the back pages
    back_pages_unreversed = back_reader.pages[::-1]

    # Interleave the pages from front and back PDFs
    for front_page, back_page in zip(front_reader.pages, back_pages_unreversed):
        writer.add_page(front_page)  # Add front page
        writer.add_page(back_page)   # Add corresponding back page (after unreversed)

    # Write the merged PDF to a file
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Merged PDF saved as {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Merge two PDF files representing the front and back pages of double-sided documents.")
    
    parser.add_argument('front_pages', type=str, help='Path to the PDF file containing front pages')
    parser.add_argument('back_pages_reversed', type=str, help='Path to the PDF file containing back pages (in reverse order)')
    parser.add_argument('output', type=str, help='Path to save the merged PDF file')
    
    args = parser.parse_args()
    
    merge_pdfs(args.front_pages, args.back_pages_reversed, args.output)

if __name__ == "__main__":
    main()

# usage:
# python merge_pdfs.py tmp/front_pages.pdf tmp/back_pages_reversed.pdf tmp/merged_document.pdf