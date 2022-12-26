import PyPDF2

with open('Resultado-PAS1.pdf', 'rb') as f:
    pdf = PyPDF2.PdfReader(f)
    count = 0
    with open('PAS1.txt', 'w') as txt:
        for page in pdf.pages:
            if count == 0:
                txt.write(page.extract_text()[994:].replace('\n', ''))
                # print(page.extract_text()[994:])
            elif count < 9:
                txt.write(page.extract_text()[4:].replace('\n', ''))
                # print(page.extract_text()[4:])
            elif count < 99:
                txt.write(page.extract_text()[5:].replace('\n', ''))
                # print(pdf.pages[50].extract_text()[6:])
            elif count < 239:
                txt.write(page.extract_text()[6:].replace('\n', ''))
                # print(pdf.pages[120].extract_text()[6:])
            elif count == 239:
                txt.write(page.extract_text()[6:3351].replace('\n', ''))
                # print(pdf.pages[239].extract_text()[6:3351])
                txt.write(' / ')
                txt.write(page.extract_text()[3753:4212].replace('\n', ''))
                # print(pdf.pages[239].extract_text()[3753:4212])

            count += 1
