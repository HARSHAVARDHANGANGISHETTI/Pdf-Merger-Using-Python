# main code
from PyPDF2 import PdfWriter
merger = PdfWriter()
pdfs=[]
n = int(input("Enter the number of PDFs to merge: "))
for i in range(0,n):
    name = input(f"enter the name of PDF {i+1}:")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)    
merger.write("merged.pdf")    
merger.close()
print("PDFs merged successfully into 'merged.pdf'")