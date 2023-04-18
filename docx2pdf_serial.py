import time
from docx2pdf import convert

files = [
        'doc1.docx','doc2.docx','doc3.docx','doc4.docx','doc5.docx',
        'doc6.docx','doc7.docx','doc8.docx','doc9.docx','doc10.docx'
        ]

t1 = time.perf_counter()
def convertToPDF():    
    for file in files:    
        convert(file,"ConvertedPDF_Serial/")   
        print(f" " + file + " was converted\n")     

convertToPDF()

t2 = time.perf_counter()
print('|---------------------------------|')
print(f'|---Finished in {t2-t1} seconds---|')
print('|---------------------------------|')