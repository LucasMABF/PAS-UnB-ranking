import PyPDF4

with open('Resultados-PAS3.pdf', 'rb') as f:
    pdf = PyPDF4.PdfFileReader(f)
    count = 0
    with open('PAS3.txt', 'w', encoding="utf-8") as txt:
        for page in pdf.pages:
            if count == 99:
                txt.write(page.extractText()[2508:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(page.extractText()[2508:])
            elif count > 99:
                txt.write(page.extractText().replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(page.extractText())

            # fiz o resto na mão
            count += 1
