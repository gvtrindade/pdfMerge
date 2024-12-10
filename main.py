import sys
import os

import img2pdf
from PIL import Image
from pypdf import PdfWriter


def main():
    if len(sys.argv) < 2 or len(sys.argv) == 1:
        print("Usage: pdfmerge file.pdf/jpg <file2.pdf/jpg> ... <-o output.pdf>")
        sys.exit()

    output = PdfWriter()
    if "-o" in sys.argv:
        file_paths = sys.argv[1:-1]
    else:
        file_paths = sys.argv[1:]
    converted = []

    for path in file_paths:
        ext = path.split(".")[-1]
        if ext == "pdf":
            output.append(path)
        elif ext in ["jpg", "png", "jpeg"]:
            new_pdf = convert_image(path)
            converted.append(new_pdf)
            output.append(new_pdf)
        else:
            print("Only PDF and image files are supported")
            sys.exit()

    final_name = f"{file_paths[0].rsplit(".", 1)[0]}_merged.pdf"

    if "-o" in sys.argv:
        i = sys.argv.index("-o") + 1
        final_name = sys.argv[i]

    output.write(final_name)
    output.close()
    
    for new_file in converted:
        os.remove(new_file)
    
    sys.exit()

def convert_image(path):
    image = Image.open(path)
    pdf_bytes = img2pdf.convert(image.filename)
    image.close()

    pdf = f"{path.rsplit(".", 1)[0]}.pdf"
    with open(pdf, "wb") as f:
        f.write(pdf_bytes)
    
    return pdf


if __name__ == "__main__":
    main()
