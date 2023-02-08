import mysql.connector as sql

db = sql.connect(host='localhost', user='root', password='')
cursor = db.cursor()
cursor.execute('USE Resultados_PAS')
cursor.execute('SELECT `nome`, `Nota Final PAS2`, `somatório escores brutos PAS2`, `nota redação PAS2`,'
               ' `nota item tipo D PAS2` FROM `resultados_PAS` WHERE `Nota Final PAS2` != 0 '
               'ORDER BY `Nota Final PAS2` DESC;')

result = cursor.fetchall()

with open('Notas_PAS2.js', 'w') as f:
    f.write("function getNotasPAS2(){\n")
    f.write("    return [\n")
    for registro in result:
        f.write('    ' + str(registro).replace("(", "[").replace(")", "]") + ',\n')
    pos = f.tell()
    f.seek(pos - 3)
    f.write('\n')
    f.write("    ];\n")
    f.write('}\n')
