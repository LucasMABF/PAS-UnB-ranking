import mysql.connector as sql

db = sql.connect(host='localhost', user='root', password='')
cursor = db.cursor()
cursor.execute('USE Resultados_PAS')
cursor.execute('SELECT `nome`, `Nota Final PAS3`, `somatório escores brutos PAS3`, `nota redação PAS3`,'
               ' `nota item tipo D PAS3` FROM `resultados_PAS` WHERE `Nota Final PAS3` != 0 '
               'ORDER BY `Nota Final PAS3` DESC;')

result = cursor.fetchall()

with open('Notas_PAS3.js', 'w') as f:
    f.write("function getNotasPAS3(){\n")
    f.write("    return [\n")
    for registro in result:
        f.write('    ' + str(registro).replace("(", "[").replace(")", "]") + ',\n')
    pos = f.tell()
    f.seek(pos - 3)
    f.write('\n')
    f.write("    ];\n")
    f.write('}\n')
