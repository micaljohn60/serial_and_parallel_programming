import time
import concurrent.futures
from docx2pdf import convert

files = [
         'doc1.docx','doc2.docx','doc3.docx','doc4.docx','doc5.docx',
         'doc6.docx','doc7.docx','doc8.docx','doc9.docx','doc10.docx'
        ]

def convertToPDF(file):    
   
    convert(file,"ConvertedPDF_Parallel/")
    print(file ,"was converted")  

if __name__ == '__main__':
    t1 = time.perf_counter()s
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(convertToPDF,files)

    t2 = time.perf_counter()
    print('|---------------------------------|')
    print(f'|---Finished in {t2-t1} seconds---|')
    print('|---------------------------------|')