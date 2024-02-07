import mysql.connector as sql

db = sql.connect(host='localhost', user='root', password='')
cursor = db.cursor()
cursor.execute('USE Resultados_PAS')
cursor.execute('SELECT `nome`, `argumento final`, `Nota Final PAS1`, `Nota Final PAS2`, `Nota final PAS3`,'
               ' `curso`, `posição curso` '
               'FROM `resultados_PAS` ORDER BY `argumento final` DESC;')

result = cursor.fetchall()

with open('final.js', 'w', encoding="utf-8") as f:
    f.write("function getFinal(){\n")
    f.write("    return [\n")
    for registro in result:
        f.write('    ' + str(registro).replace("(", "[").replace(")", "]").replace("None", "'não escolheu'") + ',\n')
    pos = f.tell()
    f.seek(pos - 3)
    f.write('\n')
    f.write("    ];\n")
    f.write('}\n')
