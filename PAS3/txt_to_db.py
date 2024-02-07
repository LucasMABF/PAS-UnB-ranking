import mysql.connector as sql

db = sql.connect(host='localhost', user='root', password='')
cursor = db.cursor()
cursor.execute('USE Resultados_PAS')

cursor.execute('ALTER TABLE `resultados_PAS` '
               'ADD COLUMN IF NOT EXISTS `somatório escores brutos PAS3` FLOAT NOT NULL, '
               'ADD COLUMN IF NOT EXISTS`nota item tipo D PAS3` FLOAT NOT NULL, '
               'ADD COLUMN IF NOT EXISTS`nota redação PAS3` FLOAT NOT NULL,'
               'ADD COLUMN IF NOT EXISTS`argumento final` FLOAT NOT NULL,'
               'ADD COLUMN IF NOT EXISTS`curso` VARCHAR(100) CHARSET utf8 COLLATE utf8_general_ci,'
               'ADD COLUMN IF NOT EXISTS`posição curso` INT not null;')


with open('PAS3.txt', encoding="utf-8") as f:
    lines = f.readlines()
    count_already_in_PAS2 = 0
    count_new_students = 0
    curso = ""
    for line in lines:
        fields = line.split(',')

        if len(fields) == 1:
            curso = fields[0].strip();
            continue

        cursor.execute('Select * from `resultados_PAS`'
                       'WHERE `número inscrição` = %s;', (fields[0], ))
        result = cursor.fetchall()
        if len(result) == 1:
            count_already_in_PAS2 += 1
            cursor.execute('UPDATE `resultados_PAS` set `somatório escores brutos PAS3` = %s'
                           ' WHERE `número inscrição` = %s;', (float(fields[8]) + float(fields[9]), fields[0]))
            cursor.execute('UPDATE `resultados_PAS` set `curso` = %s'
                           ' WHERE `número inscrição` = %s;', (curso, fields[0]))
            cursor.execute('UPDATE `resultados_PAS` set `nota redação PAS3` = %s'
                           ' WHERE `número inscrição` = %s;', (fields[10], fields[0]))
            cursor.execute('UPDATE `resultados_PAS` set `argumento final` = %s'
                           ' WHERE `número inscrição` = %s;', (fields[11], fields[0]))
            cursor.execute('UPDATE `resultados_PAS` set `posição curso` = %s'
                           ' WHERE `número inscrição` = %s;', (fields[12], fields[0]))

        elif len(result) == 0:
            count_new_students += 1
        else:
            print("Error wtf")

    db.commit()

with open("tipo_d.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        fields = line.split(',')

        cursor.execute('Select * from `resultados_PAS`'
                       'WHERE `número inscrição` = %s;', (fields[0], ))
        result = cursor.fetchall()
        if len(result) == 1:
            count_already_in_PAS2 += 1
            cursor.execute('UPDATE `resultados_PAS` set `nota item tipo D PAS3` = %s'
                           ' WHERE `número inscrição` = %s;', (fields[2], fields[0]))

        elif len(result) == 0:
            print("error")
        else:
            print("Error wtf")

    db.commit()

cursor.execute('ALTER TABLE `resultados_PAS` '
               'ADD COLUMN `Nota Final PAS3` FLOAT NOT NULL '
               'DEFAULT (`somatório escores brutos PAS3` + `nota item tipo D PAS3` + `nota redação PAS3`);')

cursor.execute('SELECT COUNT(*) FROM `resultados_PAS`;')  # 19568
result = cursor.fetchall()
print(f'Estudantes do PAS1/2 que fizeram PAS 3: {count_already_in_PAS2}')  # 8025
print(f'Só PAS3: {count_new_students} deveria ser 0')  # 0
print(result)
