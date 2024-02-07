import PyPDF4

with open('Resultados-PAS3.pdf', 'rb') as f:
    pdf = PyPDF4.PdfFileReader(f)
    count = 0
    with open('tipo_d.txt', 'w', encoding="utf-8") as txt:
        for page in pdf.pages:
            if count == 0:
                txt.write(page.extractText()[1004:].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                #print(page.extractText()[1004:])
            elif count == 99:
                txt.write(page.extractText()[:259].replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))
                # print(page.extractText()[:259])
                break
            else:
                txt.write(page.extractText().replace('\n', '').replace(' / ', '\n').replace('/ ', '\n').replace(', ', ','))

            count += 1

