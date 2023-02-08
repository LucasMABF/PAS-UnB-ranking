import mysql.connector as sql

db = sql.connect(host='localhost', user='root', password='')
cursor = db.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS `Resultados_PAS` DEFAULT CHARACTER SET utf8 '
               'DEFAULT COLLATE utf8_general_ci')
cursor.execute('USE Resultados_PAS')
cursor.execute('CREATE TABLE IF NOT EXISTS `resultados_PAS`('
               '`número inscrição` INT NOT NULL, '
               '`nome` VARCHAR(75), '
               '`somatório escores brutos PAS1` FLOAT NOT NULL, '
               '`nota item tipo D PAS1` FLOAT NOT NULL, '
               '`nota redação PAS1` FLOAT NOT NULL, '
               'PRIMARY KEY(`número inscrição`)'
               ') DEFAULT CHARSET = utf8;')

with open('PAS1.txt') as f:
    lines = f.readlines()
    for line in lines:
        fields = line.split(',')
        cursor.execute('INSERT INTO `resultados_PAS` VALUES (%s, %s, %s, %s, %s);'
                       , (fields[0], fields[1], fields[4], fields[5], fields[6].strip()))

    db.commit()

cursor.execute('ALTER TABLE `resultados_PAS` '
               'ADD COLUMN `Nota Final PAS1` FLOAT NOT NULL '
               'DEFAULT (`somatório escores brutos PAS1` + `nota item tipo D PAS1` + `nota redação PAS1`);')


cursor.execute('SELECT COUNT(*) FROM `resultados_PAS`;')  # 15783
result = cursor.fetchall()
print(result)
