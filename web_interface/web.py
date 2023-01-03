from flask import Flask, render_template, request, session
import mysql.connector as sql
from dotenv import load_dotenv
import os


db = sql.connect(host='localhost', user='root', password='')
cursor = db.cursor()
cursor.execute('USE Resultados_PAS')

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRETKEY')


@app.route('/', methods=['GET', 'POST'])
def index():
    registros = []
    if request.method == 'POST':
        if 'orderby' in request.form.keys():
            if request.form['orderby'] == '1':
                if 'registros' in session:
                    if len(session['registros']) != 0:
                        registros = session['registros']
                        t = f'{session["registros"]}'.replace('[', '(').replace(']', ')')
                        cursor.execute('SELECT Ranking, nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, '
                                       '`nota redação PAS1`, `nota item tipo D PAS1` FROM (SELECT ROW_NUMBER() OVER '
                                       '(ORDER BY `Nota Final PAS1` DESC) AS Ranking, '
                                       'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                       '`nota item tipo D PAS1` FROM resultados_PAS) Ranking '
                                       f'WHERE nome IN {t};')
                    else:
                        cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `Nota Final PAS1` DESC) AS Ranking, '
                                       'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                       '`nota item tipo D PAS1` FROM resultados_PAS')
                else:
                    cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `Nota Final PAS1` DESC) AS Ranking, '
                                   'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                   '`nota item tipo D PAS1` FROM resultados_PAS')
            elif request.form['orderby'] == '2':
                if 'registros' in session:
                    if len(session['registros']) != 0:
                        registros = session['registros']
                        t = f'{session["registros"]}'.replace('[', '(').replace(']', ')')
                        cursor.execute('SELECT Ranking, nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, '
                                       '`nota redação PAS1`, `nota item tipo D PAS1` FROM (SELECT ROW_NUMBER() OVER '
                                       '(ORDER BY `somatório escores brutos PAS1` DESC) AS Ranking, '
                                       'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                       '`nota item tipo D PAS1` FROM resultados_PAS) Ranking '
                                       f'WHERE nome IN {t};')
                    else:
                        cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `somatório escores brutos PAS1` DESC)'
                                       ' AS Ranking, '
                                       'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                       '`nota item tipo D PAS1` FROM resultados_PAS')
                else:
                    cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `somatório escores brutos PAS1` DESC)'
                                   ' AS Ranking, '
                                   'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                   '`nota item tipo D PAS1` FROM resultados_PAS')
            elif request.form['orderby'] == '3':
                if 'registros' in session:
                    if len(session['registros']) != 0:
                        registros = session['registros']
                        t = f'{session["registros"]}'.replace('[', '(').replace(']', ')')
                        cursor.execute('SELECT Ranking, nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, '
                                       '`nota redação PAS1`, `nota item tipo D PAS1` FROM (SELECT ROW_NUMBER() OVER '
                                       '(ORDER BY `nota redação PAS1` DESC) AS Ranking, '
                                       'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                       '`nota item tipo D PAS1` FROM resultados_PAS) Ranking '
                                       f'WHERE nome IN {t};')
                    else:
                        cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `nota redação PAS1` DESC) AS Ranking, '
                                       'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                       '`nota item tipo D PAS1` FROM resultados_PAS')
                else:
                    cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `nota redação PAS1` DESC) AS Ranking, '
                                   'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                   '`nota item tipo D PAS1` FROM resultados_PAS')
            elif request.form['orderby'] == '4':
                if 'registros' in session:
                    if len(session['registros']) != 0:
                        registros = session['registros']
                        t = f'{session["registros"]}'.replace('[', '(').replace(']', ')')
                        cursor.execute('SELECT Ranking, nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, '
                                       '`nota redação PAS1`, `nota item tipo D PAS1` FROM (SELECT ROW_NUMBER() OVER '
                                       '(ORDER BY `nota item tipo D PAS1` DESC) AS Ranking, '
                                       'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                       '`nota item tipo D PAS1` FROM resultados_PAS) Ranking '
                                       f'WHERE nome IN {t};')
                    else:
                        cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `nota item tipo D PAS1` DESC) AS Ranking, '
                                       'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                       '`nota item tipo D PAS1` FROM resultados_PAS')
                else:
                    cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `nota item tipo D PAS1` DESC) AS Ranking, '
                                   'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                                   '`nota item tipo D PAS1` FROM resultados_PAS')

            return render_template('index.html', content=cursor.fetchall(), orderby=int(request.form['orderby']),
                                                                                        registros=registros)
        elif 'registros' in request.form.keys():
            if 'registros' in session:
                session['registros'].append(request.form['registros'])
                session.modified = True
            else:
                session['registros'] = [request.form['registros']]

            registros = session['registros']
            t = f'{session["registros"]}'.replace('[', '(').replace(']', ')')
            cursor.execute('SELECT Ranking, nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, '
                           '`nota redação PAS1`, `nota item tipo D PAS1` FROM (SELECT ROW_NUMBER() OVER '
                           '(ORDER BY `Nota Final PAS1` DESC) AS Ranking, '
                           'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                           '`nota item tipo D PAS1` FROM resultados_PAS) Ranking '
                           f'WHERE nome IN {t};')
            return render_template('index.html', content=cursor.fetchall(), orderby=1, registros=registros)
        elif 'closeregistro' in request.form.keys():
            session['registros'].remove(request.form['closeregistro'])
            session.modified = True
            registros = session['registros']
            if len(session['registros']) != 0:
                t = f'{session["registros"]}'.replace('[', '(').replace(']', ')')
                cursor.execute('SELECT Ranking, nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, '
                               '`nota redação PAS1`, `nota item tipo D PAS1` FROM (SELECT ROW_NUMBER() OVER '
                               '(ORDER BY `Nota Final PAS1` DESC) AS Ranking, '
                               'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                               '`nota item tipo D PAS1` FROM resultados_PAS) Ranking '
                               f'WHERE nome IN {t};')
            else:
                cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `Nota Final PAS1` DESC) AS Ranking, '
                               'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                               '`nota item tipo D PAS1` FROM resultados_PAS')

        return render_template('index.html', content=cursor.fetchall(), orderby=1, registros=registros)
    else:
        if 'registros' in session:
            if len(session['registros']) != 0:
                registros = session['registros']
                t = f'{session["registros"]}'.replace('[', '(').replace(']', ')')
                cursor.execute('SELECT Ranking, nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, '
                               '`nota redação PAS1`, `nota item tipo D PAS1` FROM (SELECT ROW_NUMBER() OVER '
                               '(ORDER BY `Nota Final PAS1` DESC) AS Ranking, '
                               'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                               '`nota item tipo D PAS1` FROM resultados_PAS) Ranking '
                               f'WHERE nome IN {t};')
            else:
                cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `Nota Final PAS1` DESC) AS Ranking, '
                               'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                               '`nota item tipo D PAS1` FROM resultados_PAS')
        else:
            cursor.execute('SELECT ROW_NUMBER() OVER (ORDER BY `Nota Final PAS1` DESC) AS Ranking, '
                           'nome, `Nota Final PAS1`, `somatório escores brutos PAS1`, `nota redação PAS1`, '
                           '`nota item tipo D PAS1` FROM resultados_PAS')
        return render_template('index.html', content=cursor.fetchall(), orderby=1, registros=registros)


if __name__ == "__main__":
    app.run(port=80, debug=True)
