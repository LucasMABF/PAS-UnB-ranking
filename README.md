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

Adicionei uma interface gráfica estática usando apenas HTML, CSS e JavaScript, por ser mais fácil de hospedar, 
no github pages. Dessa forma pretendo deixar as duas implementações nesse repositório e atualizál-las 
de acordo com a liberação das notas do PAS2 e PAS3, e criar outro repositório para hospedar o site, se for o caso. 

---
# Etapas

Etapas do processo de extração e reorganização dos dados presentes do PDF disponibilizado pela UnB por [esse link](https://cdn.cebraspe.org.br/pas/arquivos/ED_5_PAS_1_2021-2023_Res_Final_Tipo_D_e_Reda%C3%A7%C3%A3o.pdf):

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

Esse site tem as funcionalidades de ordenar de acordo com diferentes campos e selecionar registros por nome para 
mostrar apenas as pessoas selecionadas pelo usuário.

<details>
<summary>Observações de implementação</summary>
Para filtrar os registros por nome eu não achei uma maneira de pegar uma lista ou tupla em python e passar para o 
comando MySQL sem usar f strings. Que não é indicado por questões de segurança, porém parece que o código está bem sanitizado 
e não consegui fazer uma SQL injection, então deixei assim.
</details>

No entanto, é muito mais difícil hospedar um site com um backend, que nem esse feito com flask, por isso estou 
considerando tornar o site completamente estático, e usar JavaScript para manipular os dados que fornecerei em formato 
de uma lista em JavaScript, para não ter que usar um banco de dados. Essa abordagem tem algumas desvantagens, como a 
maior dificuldade de lidar com os dados em JavaScript e não em um banco de dados, e ter que mandar todos os dados, que 
estão em grande quantidade, para o usuário.

Se eu for postar esse site, e torná-lo acessível, é muito mais fácil trocar toda a lógica do backend por uma de página 
estática. Assim eu posso hospedar no GitHub pages, de graça.


---

Criei outra implementação do site para mostrar os resultados de maneira estática, o que facilita a hospedagem do site. 
Troquei o banco de dados por uma longa lista em JavaScript e usei JavaScript para ordenar e manipular esses dados.

Para transformar o banco de dados em JavaScript, e fazer os dados compatíveis com a implementação estática 
criei o código python no arquivo `db_to_js_ordered.py`

- Esse código vai criar o arquivo `Notas_PAS1.js`, a partir do banco de dados, que vai ter uma função que retorna uma 
lista coms todos os valores já ordenados pela soma dos escores brutos, com a nota da Redação e da questão tipo D.

<details>
<summary>Observações de implementação</summary>
Eu decidi já colocar os resultados ordenados pelo campo que acredito ser o mais relevante, a soma de todas as notas, porque 
assim o JavaScript que roda na máquina do usuário vai ficar um pouco menos sobrecarregado, já que mandar todos os dados para 
o usúario já é muito pesado.

Também decidi colocar esses dados dentro de uma função que retorna essa lista, porque acredito que para ordenar de novo a lista 
que foi ordenada por outro campo pelo usuário, é melhor recarregar toda a lista, que já vem ordenada, do que pedir para o 
JavaScript ordenar de novo.

Não tenho certeza se minha lógica por trás dessa implementação está muito correta, até porque achei os tempos de carregamento 
muito parecidos. Mas a minha ideia era que para ordenar a lista de novo o código deveria rodar em O(n log(n)) e só para carregar 
a lista novamente deveria ser O(n) ou até O(1), para n sendo o número de alunos registrados. 
Mas não tenho certeza se esses dados  estão corretos

Depois de chamar a função que retorna os dados, eles são armazenados em uma variável global, que achei mais fácil de implementar, 
já que todo o site tem que acessar esses dados. No entanto não sei se essa é a melhor implementação, devido à muitas críticas que 
existem em relação ao uso de variáveis globais.
</details>

Depois de ter o arquivo em JavaScript com os dados, adicionei ele à pasta do site estático, que seria a pasta hospedada e mandada 
para o usuário. Esse arquivo é chamado pelo HTML antes do `index.js`.

O `index.js` é o responsável por manipular os dados do outro arquivo e mostrá-los em ordem diferentes e filtrá-los.

O filtro serve para mostrar apenas os dados de pessoas específicas, que são filtradas por nome. Essas pessoas são adicionadas à uma outra
lista que é uma variável global, e apenas as pessoas nessa lista são mostradas. Esse filtro só é aplicado depois do ordenamento de todos 
os registros, para assim manter o número do ranking de cada um. 

<details>
<summary> Observações de implementação</summary>
Deixei a variável do filtro global, assim como a dos dados, porque mais de uma função tem que usá-la, e achei mais prático assim, 
mas de novo, não sei se isso cria algum problema ou se existe um outro jeito melhor e mais prático também.

Na hora de mostrar os dados o código passa por todas os registros e seleciona os que os nomes coincidem, o que não é muito prático, mas 
acredito ser a única forma. Para melhorar um pouco a performance adicionei uma condição que vê se todos os filtros já foram vistos e 
asssim pula o resto dos registros. Mas não sei se isso muda muita coisa.
</details>
