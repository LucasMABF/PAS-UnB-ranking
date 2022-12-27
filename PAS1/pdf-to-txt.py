import PyPDF4

with open('Resultado-PAS1.pdf', 'rb') as f:
    pdf = PyPDF4.PdfFileReader(f)
    count = 0
    with open('PAS1.txt', 'w') as txt:
        for page in pdf.pages:
            if count == 0:
                txt.write(page.extractText()[1012:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(page.extractText()[1012:])
            elif count < 9:
                txt.write(page.extractText()[6:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(page.extractText()[6:])
            elif count < 99:
                txt.write(page.extractText()[7:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(pdf.pages[50].extractText()[7:])
            elif count < 239:
                txt.write(page.extractText()[8:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(pdf.pages[120].extractText()[8:])
            elif count == 239:
                txt.write(page.extractText()[8:3359].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(pdf.pages[239].extractText()[8:3359])
                txt.write('\n')
                txt.write(page.extractText()[3767:4227].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(pdf.pages[239].extractText()[3767:4227])

            count += 1
