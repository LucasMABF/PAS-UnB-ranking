import mysql.connector as sql

db = sql.connect(host='localhost', user='root', password='')
cursor = db.cursor()
cursor.execute('USE Resultados_PAS')
cursor.execute('SELECT `nome`, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`,'
               ' `nota item tipo D PAS1` FROM `resultados_PAS` ORDER BY `Nota Final PAS1` DESC;')

result = cursor.fetchall()

with open('Notas_PAS1.js', 'w') as f:
    f.write("function getNotasPAS1(){\n")
    f.write("    return [\n")
    for registro in result:
        f.write('    ' + str(registro).replace("(", "[").replace(")", "]") + ',\n')
    pos = f.tell()
    f.seek(pos - 3)
    f.write('\n')
    f.write("    ];\n")
    f.write('}\n')
