# PAS(UnB) ranking
 Esse repositório é feito para criar um banco de dados SQL dos resultados do PAS(Programa de Avaliação Seriada) da UnB.
Para conseguir organizar e manipular os resultados,
 para gerar facilmente a posição de cada resultado em relação aos outros.

Isso será feito com código python, misturado com MySQL, para extrair os dados do PDF fornecido pela UnB, 
que não mostra o ranking e a nota final.

Por enquanto apenas está disponível o PAS1 do programa 2021-2023, mas quando os resultados do PAS2, e eventualmente
PAS 3, pretendo atualizar o banco de dados com scripts diferentes, que serão postados com o decorrer do tempo.

Também considero criar uma ferramenta online usando Flask, para mostrar esses dados de diferentes formas e
mostrar mais facilmente a posição geral.

---
# Etapas

Etapas do processo de extração e reorganização dos dados presentes do PDF disponibilizado pela Unb:

1. Rodar o código python no arquivo `PAS1-pdf-to-txt.py` no mesmo diretório que o PDF.

- isso vai gerar um arquivo `.txt` que vai ser muito mais fácil de manipular com todos os registros do PDF.
- O arquivo têm apenas uma linha, e é dividido por `/`, sendo cada valor dos registros separados por `,`.
- __Obs__: Esse código é feito exclusivamente para extrair as informações do arquivo PDF disponibilizado com as notas
do PAS 1, do subprograma 2021-2023, uma vez que cada arquivo PDF vai ter uma formatação diferente, e no código existe
vários valores que foram "harcoded" para esse documento em específico.

2.
