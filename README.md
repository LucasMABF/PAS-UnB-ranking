# PAS(UnB) ranking
- Esse repositório é feito para organizar e manipular os dados do resultado do PAS(Programa de Avaliação Seriada)da UnB,
para gerar facilmente um ranking geral de todas as notas.

- Isso foi feito usando scripts em python para extrair dados dos PDFs disponibilizados pela UnB, MySQL para ajudar a 
organizar os dados e uma interface gráfica web estática.

- Optei por um site estático por ser mais fácil de hospedar, se fosse o caso, no github pages, porém antes dessa abordagem
eu implementei um site com Flask, e deixei essa implementação no repositório, mas está desatualizada com as novas notas 
e alterações na interface. Essa nova abordagem tem algumas desvantagens, como maior dificuldade de lidar com os dados em
JavaScript no lugar de um banco de dados, e ter que fornecer todos os dados, que estão em grande quantidade, para o usuário.

---
# Acessar interface gráfica

- Eu criei uma interface gráfica que permite mostrar os resultados e o ranking de todas as etapas do PAS, 
e o resultado geral, ordená-los de acordo com diferentes campos, filtrá-los por nome ou por curso.

- Eu decidi não disponibilizar essa página, portanto se quiser ter acesso, terá que baixar a pasta 
`static_web_interface` e accessar localmente, abrindo o arquivo `index.html`.
- 
---
# Etapas

Etapas do processo de extração e reorganização dos dados presentes do PDF disponibilizado pela UnB por [essa página](https://www.cebraspe.org.br/pas/subprogramas/2021_2023/3):

1. Extrair os dados do PDF com as notas

- Os scripts que fazem isso são os `pdf-t0-txt.py`, que extraem as notas para um arquivo txt.

- Esses scripts são apenas a feitos para extrair as notas de cada PDF específico, uma vez que os valores são *hardcoded* 
eu não criei nada elaborado para lidar com isso melhor.

- O arquivo é dividido por linhas, e cada linha é dividida por `,` para separar os valores.

2. Adicionar dados em um banco de dados MySQL para melhor manipulação

- Os scripts `txt_to_db.py` pegam os dados dos arquivos txt extraidos e adicionam à um banco de dados, para isso é
necessário estar rodando um banco de dados.

3. Ordenar os dados e colocá-los em javascript para ser usado em um site estático

- Os script `db_to_js_ordered.py` criam um arquivo JavaScript com os registros disponibilizados em uma lista 
já ordenados, esse arquivo fornece uma função que retorna essa lista.


<details>
<summary>Observações de implementação</summary>

- Eu decidi já colocar os resultados ordenados pelo campo que acredito ser o mais relevante, o argumento final, porque 
assim o JavaScript que roda na máquina do usuário vai ficar um pouco menos sobrecarregado, já que mandar todos os dados para 
o usúario já é muito pesado.

- Também decidi colocar esses dados dentro de uma função que retorna essa lista, porque acredito que para ordenar de novo a lista 
que foi ordenada por outro campo pelo usuário, é melhor recarregar toda a lista, que já vem ordenada, do que pedir para o 
JavaScript ordenar de novo.

- Não tenho certeza se minha lógica por trás dessa implementação está muito correta, até porque achei os tempos de carregamento 
muito parecidos. Mas a minha ideia era que para ordenar a lista de novo o código deveria rodar em O(n log(n)) e só para carregar 
a lista novamente deveria ser O(n) ou até O(1), para n sendo o número de alunos registrados. 
Mas não tenho certeza se esses dados  estão corretos.

</details>
