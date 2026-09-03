from pypdf import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many PDF Do you wnat to merge?\n"))
for i in range (0, n):
    name = input(f"Enter the name of PDF {i + 1}: ")
    pdfs.append(name)


for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_PDF.pdf")
merger.close()