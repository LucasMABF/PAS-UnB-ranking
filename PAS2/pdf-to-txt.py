import PyPDF4

with open('Resultado-PAS2.pdf', 'rb') as f:
    pdf = PyPDF4.PdfFileReader(f)
    count = 0
    with open('PAS2.txt', 'w') as txt:
        for page in pdf.pages:
            if count == 0:
                txt.write(page.extractText()[1041:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(page.extractText()[1041:])
            elif count < 9:
                txt.write(page.extractText()[6:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(page.extractText()[6:])
            elif count < 99:
                txt.write(page.extractText()[7:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(pdf.pages[50].extractText()[7:])
            elif count < 233:
                txt.write(page.extractText()[8:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(pdf.pages[120].extractText()[8:])
            elif count == 233:
                txt.write(page.extractText()[8:4818].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(pdf.pages[233].extractText()[8:4818])
                txt.write('\n')
                txt.write(pdf.pages[234].extractText()[194:1198].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                #print(pdf.pages[234].extractText()[194:1198])

            count += 1
