import mysql.connector as sql

db = sql.connect(host='localhost', user='root', password='')
cursor = db.cursor()
cursor.execute('USE Resultados_PAS')
cursor.execute('SELECT `nome`, `Nota PAS1 E PAS2`, `Nota Final PAS1`, `Nota Final PAS2` '
               'FROM `resultados_PAS` ORDER BY `Nota PAS1 E PAS2` DESC;')

result = cursor.fetchall()

with open('Notas_PAS1-PAS2.js', 'w') as f:
    f.write("function getNotasPAS1_PAS2(){\n")
    f.write("    return [\n")
    for registro in result:
        f.write('    ' + str(registro).replace("(", "[").replace(")", "]") + ',\n')
    pos = f.tell()
    f.seek(pos - 3)
    f.write('\n')
    f.write("    ];\n")
    f.write('}\n')
