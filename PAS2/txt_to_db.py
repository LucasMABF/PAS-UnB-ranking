import mysql.connector as sql

db = sql.connect(host='localhost', user='root', password='')
cursor = db.cursor()
cursor.execute('USE Resultados_PAS')

cursor.execute('ALTER TABLE `resultados_PAS` '
               'ADD COLUMN `somatório escores brutos PAS2` FLOAT NOT NULL, '
               'ADD COLUMN `nota item tipo D PAS2` FLOAT NOT NULL, '
               'ADD COLUMN `nota redação PAS2` FLOAT NOT NULL;')

with open('PAS2.txt') as f:
    lines = f.readlines()
    count_already_in_PAS1 = 0
    count_new_students = 0
    for line in lines:
        fields = line.split(',')
        cursor.execute('Select * from `resultados_PAS`'
                       'WHERE `número inscrição` = %s;', (fields[0], ))
        result = cursor.fetchall()
        if len(result) == 1:
            count_already_in_PAS1 += 1
            cursor.execute('UPDATE `resultados_PAS` set `somatório escores brutos PAS2` = %s'
                           ' WHERE `número inscrição` = %s;', (fields[4], fields[0]))
            cursor.execute('UPDATE `resultados_PAS` set `nota item tipo D PAS2` = %s'
                           ' WHERE `número inscrição` = %s;', (fields[5], fields[0]))
            cursor.execute('UPDATE `resultados_PAS` set `nota redação PAS2` = %s'
                           ' WHERE `número inscrição` = %s;', (fields[6].strip(), fields[0]))
        elif len(result) == 0:
            count_new_students += 1
            cursor.execute('INSERT INTO `resultados_PAS` (`número inscrição`, `nome`, `somatório escores brutos PAS2`, '
                           '`nota item tipo D PAS2`, `nota redação PAS2`) '
                           'VALUES (%s, %s, %s, %s, %s);'
                           , (fields[0], fields[1], fields[4], fields[5], fields[6].strip()))
        else:
            print("Error wtf")

    db.commit()

cursor.execute('ALTER TABLE `resultados_PAS` '
               'ADD COLUMN `Nota Final PAS2` FLOAT NOT NULL '
               'DEFAULT (`somatório escores brutos PAS2` + `nota item tipo D PAS2` + `nota redação PAS2`);')

cursor.execute('SELECT COUNT(*) FROM `resultados_PAS`;')  # 15431
result = cursor.fetchall()
print(f'Estudantes do PAS1: {count_already_in_PAS1}')
print(f'Só PAS2: {count_new_students}')
print(result)

cursor.execute('ALTER TABLE `resultados_PAS` '
               'ADD COLUMN `Nota PAS1 e PAS2` FLOAT NOT NULL '
               'DEFAULT (`Nota Final PAS1` / 6 + `Nota Final PAS2` / 3);')
