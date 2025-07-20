from PyPDF2 import PdfWriter
merger = PdfWriter()
pdfs=[]
try:
    n = int(input("How many PDF do u wanna merge?\n"))

    for i in range (0,n) :
        name = input(f"Enter the name of PDF {i+1} : ")
        pdfs.append(name)
except:
    print(f"----------invalid number----------")

try :
    for pdf in pdfs:
        merger.append(pdf)
except Exception as e:
    print(f"---------------File not found: {e}------------")

merger.write("merged-pdf4.pdf")
merger.close()