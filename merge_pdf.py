"""
Merges multiple PDF files into one large file.
Requires PyPDF2
"""

import os
import sys
import os.path

from PyPDF2 import PdfFileMerger, PdfFileReader

def main():
    if len(sys.argv) < 2:
        print "No source files suppplied!"
        sys.exit(1)
        
    merger = PdfFileMerger()
    for fname in sys.argv[1:]:
        merger.append(PdfFileReader(file(fname, 'rb')))
        
    merger.write("document-output.pdf")

if __name__ == "__main__":
    main()
