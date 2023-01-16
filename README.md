# PAS(UnB) ranking
 Esse repositório é feito para criar um banco de dados SQL dos resultados do PAS(Programa de Avaliação Seriada) da UnB.
Para conseguir organizar e manipular os resultados,
 para gerar facilmente a posição, um ranking, de cada resultado em relação aos outros.

Isso será feito com código python, misturado com MySQL, para extrair os dados do PDF fornecido pela UnB, 
que não mostra o ranking e a nota final.

Por enquanto apenas está disponível o PAS1 do programa 2021-2023, mas quando os resultados do PAS2, e eventualmente
PAS 3, pretendo atualizar o banco de dados com scripts diferentes, que serão postados com o decorrer do tempo.

Também considero criar uma ferramenta online usando Flask, para mostrar esses dados de diferentes formas e
mostrar mais facilmente a posição geral.

---
# Etapas

Etapas do processo de extração e reorganização dos dados presentes do PDF disponibilizado pela UnB:

1. Rodar o código python no arquivo `pdf-to-txt.py` no mesmo diretório que o PDF.

- isso vai gerar um arquivo `.txt` que vai ser muito mais fácil de manipular com todos os registros do PDF.
- O arquivo é dividido por linhas, e cada linha é dividida por `,` para separar os valores.
- __Obs__: Esse código é feito exclusivamente para extrair as informações do arquivo PDF disponibilizado com as notas
do PAS 1, do subprograma 2021-2023, uma vez que cada arquivo PDF vai ter uma formatação diferente, e no código existe
vários valores que foram "harcoded" para esse documento em específico.

2. Rodar o código python no arquivo `txt_to_db.py` com o banco de dados rodando e o arquivo criado anteriormente,
 `PAS1.txt`, no mesmo diretório.
- Esse código vai gerar os registros em um banco de dados, `Resultados_PAS`, a partir do arquivo `txt.`.

Depois dos dados já em um banco de dados, eles são muito mais fáceis de manipular, e de organizar de acordo com as 
notas, a partir do `ORDER BY` do MySQL.

Depois disso criei uma interface gráfica, por meio do flask, que mostra em um site toda a informação do banco de dados, 
permitindo diferentes organizações e filtros. O python acessa os dados do banco de dados e fornece para o usuário de 
uma maneira formatada em HTML e CSS.

No entanto, é muito mais difícil hospedar um site com um backend, que nem esse feito com flask, por isso estou 
considerando tornar o site completamente estático, e usar JavaScript para manipular os dados que fornecerei em formato 
de uma lista em JavaScript, para não ter que usar um banco de dados. Essa abordagem tem algumas desvantagens, como a 
maior dificuldade de lidar com os dados em JavaScript e não em um banco de dados, e ter que mandar todos os dados, que 
estão em grande quantidade, para o usuário.

Se eu for postar esse site, e torná-lo acessível, é muito mais fácil trocar toda a lógica do backend por uma de página 
estática. Assim eu posso hospedar no GitHub pages, de graça.
