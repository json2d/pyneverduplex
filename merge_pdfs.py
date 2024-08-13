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

# Paths to the PDF files
front_pages_path = "tmp/front_pages.pdf"
back_pages_reversed_path = "tmp/back_pages_reversed.pdf"
output_path = "tmp/merged_document.pdf"

# Merge the PDFs
merge_pdfs(front_pages_path, back_pages_reversed_path, output_path)
