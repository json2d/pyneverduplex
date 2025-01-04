import argparse
import os
from merge_pdfs import merge_pdfs

def main():
    parser = argparse.ArgumentParser(description="Merge two PDF files representing the front and back pages of double-sided documents.")
    
    parser.add_argument('output', type=str, help='Path to save the merged PDF file')
    
    args = parser.parse_args()
    
    output_wo_ext = os.path.splitext(args.output)[0]
    merge_pdfs(f'{output_wo_ext}__f.pdf', f'{output_wo_ext}__br.pdf', args.output)

if __name__ == "__main__":
    main()

# usage:
# python qmerge_pdfs.py tmp/some_pages.pdf