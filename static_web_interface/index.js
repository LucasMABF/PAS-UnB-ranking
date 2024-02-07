let data = getFinal();
filter = [];


function load_final(){
    data = getFinal();
    let orderby = document.getElementById('orderby');
    orderby.innerHTML = '';
    let header = document.getElementById('header');
    header.innerHTML = '';
    let HeaderRow = document.createElement('tr');
    let titles = ['Posição', 'Nome', 'Argumento final', 'Nota Final PAS1', 'Nota Final PAS2', 'Nota Final PAS 3',
     'Curso', 'posição curso'];
    for (let t = 0; t < titles.length; t++){
        let NewHeader = document.createElement('th');
        NewHeader.innerHTML = titles[t];
        HeaderRow.appendChild(NewHeader);
        if(t > 1 && t < 6){
            let newOrder = document.createElement('option');
            newOrder.value = t - 1;
            newOrder.innerHTML = titles[t];
            orderby.appendChild(newOrder)
        }
    }
    header.appendChild(HeaderRow);
    let title = document.getElementById('title');
    title.innerHTML = 'Ranking Resultados PAS';
    renderResults();
}

function load_PAS1(){
    data = getNotasPAS1();
    let orderby = document.getElementById('orderby');
    orderby.innerHTML = '';
    let header = document.getElementById('header');
    header.innerHTML = '';
    let HeaderRow = document.createElement('tr');
    let titles = ['Posição', 'Nome', '<abbr title="Somatório escores brutos + Redação + item tipo D">Nota Final</abbr>', 'Somatório Escores Brutos', 'Nota Redação', 'Nota Item Tipo D'];
    for (let t = 0; t < titles.length; t++){
        let NewHeader = document.createElement('th');
        NewHeader.innerHTML = titles[t];
        HeaderRow.appendChild(NewHeader);
        if( t > 1){
            let newOrder = document.createElement('option');
            newOrder.value = t - 1;
            newOrder.innerHTML = titles[t];
            orderby.appendChild(newOrder)
        }
    }
    header.appendChild(HeaderRow);
    let title = document.getElementById('title');
    title.innerHTML = 'Ranking Resultados PAS1';
    renderResults();
}

function load_PAS2(){
    data = getNotasPAS2()
    let orderby = document.getElementById('orderby');
    orderby.innerHTML = '';
    let header = document.getElementById('header');
    header.innerHTML = '';
    let HeaderRow = document.createElement('tr');
    let titles = ['Posição', 'Nome', '<abbr title="Somatório escores brutos + Redação + item tipo D">Nota Final</abbr>', 'Somatório Escores Brutos', 'Nota Redação', 'Nota Item Tipo D'];
    for (let t = 0; t < titles.length; t++){
        let NewHeader = document.createElement('th');
        NewHeader.innerHTML = titles[t];
        HeaderRow.appendChild(NewHeader);
        if( t > 1){
            let newOrder = document.createElement('option');
            newOrder.value = t - 1;
            newOrder.innerHTML = titles[t];
            orderby.appendChild(newOrder)
        }
    }
    header.appendChild(HeaderRow);
    let title = document.getElementById('title');
    title.innerHTML = 'Ranking Resultados PAS2';
    renderResults();
}
function load_PAS3(){
    data = getNotasPAS3();
    let orderby = document.getElementById('orderby');
    orderby.innerHTML = '';
    let header = document.getElementById('header');
    header.innerHTML = '';
    let HeaderRow = document.createElement('tr');
    let titles = ['Posição', 'Nome', '<abbr title="Somatório escores brutos + Redação + item tipo D">Nota Final</abbr>', 'Somatório Escores Brutos', 'Nota Redação', 'Nota Item Tipo D'];
    for (let t = 0; t < titles.length; t++){
        let NewHeader = document.createElement('th');
        NewHeader.innerHTML = titles[t];
        HeaderRow.appendChild(NewHeader);
        if( t > 1){
            let newOrder = document.createElement('option');
            newOrder.value = t - 1;
            newOrder.innerHTML = titles[t];
            orderby.appendChild(newOrder)
        }
    }
    header.appendChild(HeaderRow);
    let title = document.getElementById('title');
    title.innerHTML = 'Ranking Resultados PAS3';
    renderResults();
}

function renderResults(){
    let title = document.getElementById('title');
    if(title.innerHTML == "Ranking Resultados PAS"){
        let cursos = document.getElementById("cursos")
        curso = cursos.value;
        if (curso == ""){
            let table = document.getElementById('table-data');
            table.innerHTML = '';
            if(filter.length != 0){
                for(let i = 0; i < data.length; i++){
                    for (let k = 0; k < filter.length; k++){
                        if(data[i][0].toLowerCase().trim().includes(filter[k])){
                            let newRow = document.createElement('tr')
                            table.appendChild(newRow)
                            for(let j = 0; j <= data[i].length; j++){
                                let newTd = document.createElement('td');
                                if(j == 0){
                                    newTd.innerHTML = i + 1;
                                }else{
                                    newTd.innerHTML = data[i][j - 1];
                                }
                                newRow.appendChild(newTd);
                            }
                            break;
                        }
                    }
                }
            }else{
                for(let i = 0; i < data.length; i++){
                    let newRow = document.createElement('tr')
                    table.appendChild(newRow)
                    for(let j = 0; j <= data[i].length; j++){
                        let newTd = document.createElement('td');
                        if(j == 0){
                            newTd.innerHTML = i + 1;
                        }else{
                            newTd.innerHTML = data[i][j - 1];
                        }
                        newRow.appendChild(newTd);
                    }
                }
            }
        }else{
            let table = document.getElementById('table-data');
            table.innerHTML = '';
            if(filter.length != 0){
                for(let i = 0; i < data.length; i++){
                    for (let k = 0; k < filter.length; k++){
                        if(data[i][0].toLowerCase().trim().includes(filter[k]) && data[i][5] == curso){
                            let newRow = document.createElement('tr')
                            table.appendChild(newRow)
                            for(let j = 0; j <= data[i].length; j++){
                                let newTd = document.createElement('td');
                                if(j == 0){
                                    newTd.innerHTML = i + 1;
                                }else{
                                    newTd.innerHTML = data[i][j - 1];
                                }
                                newRow.appendChild(newTd);
                            }
                            break;
                        }
                    }
                }
            }else{
                for(let i = 0; i < data.length; i++){
                    if (data[i][5] == curso){
                        let newRow = document.createElement('tr')
                        table.appendChild(newRow)
                        for(let j = 0; j <= data[i].length; j++){
                            let newTd = document.createElement('td');
                            if(j == 0){
                                newTd.innerHTML = i + 1;
                            }else{
                                newTd.innerHTML = data[i][j - 1];
                            }
                            newRow.appendChild(newTd);
                        }
                    }
                }
            }
        }
    }else{
        let table = document.getElementById('table-data');
        table.innerHTML = '';
        if(filter.length != 0){
            for(let i = 0; i < data.length; i++){
                for (let k = 0; k < filter.length; k++){
                    if(data[i][0].toLowerCase().trim().includes(filter[k])){
                        let newRow = document.createElement('tr')
                        table.appendChild(newRow)
                        for(let j = 0; j <= data[i].length; j++){
                            let newTd = document.createElement('td');
                            if(j == 0){
                                newTd.innerHTML = i + 1;
                            }else{
                                newTd.innerHTML = data[i][j - 1];
                            }
                            newRow.appendChild(newTd);
                        }
                        break;
                    }
                }
            }
        }else{
            for(let i = 0; i < data.length; i++){
                let newRow = document.createElement('tr')
                table.appendChild(newRow)
                for(let j = 0; j <= data[i].length; j++){
                    let newTd = document.createElement('td');
                    if(j == 0){
                        newTd.innerHTML = i + 1;
                    }else{
                        newTd.innerHTML = data[i][j - 1];
                    }
                    newRow.appendChild(newTd);
                }
            }
        }
    }
}

function changeOrder(){
    let element = document.getElementById('orderby');
    let order = element.value;
    let title = document.getElementById('title');
    let max = 0
    if (title.innerHTML == 'Ranking Resultados PAS'){
        max = 6;
    }else{
        max = 4;
    }
    if (order < 2 || order > max){
        if (title.innerHTML == 'Ranking Resultados PAS1'){
            data = getNotasPAS1();
        }else if (title.innerHTML == 'Ranking Resultados PAS2'){
            data = getNotasPAS2();
        }else if (title.innerHTML == 'Ranking Resultados PAS 3'){
            data = getNotasPAS3();
        }else{
            data = getFinal();
        }
    }else{
        data.sort(function(a, b){
            if(b[order] == a[order]){
                return b[1] - a[1] // 1 must be the most important field
            }else{
                return b[order] - a[order]
            }
        })
    }
    renderResults();
}

function addToFilter(event){
    if(event.key == 'Enter' || event.srcElement.id == 'filterbutton'){
        let registroField = document.getElementById('registro')
        let registro = registroField.value.trim()
        registroField.value = ''
        if (registro.length != 0){
            let replaced = registro.toLowerCase()
            let replace_characters = [['á', 'à', 'ã', 'â'], ['é', 'ê'], ['í', 'î'], ['ó', 'ô', 'õ'], ['ú', 'û'], ['ç']]
            let replacements = ['a', 'e', 'i', 'o', 'u', 'c']
            for(let i = 0; i < replace_characters.length; i++){
                for(let j = 0; j < replace_characters[i].length; j++){
                    replaced = replaced.replace(replace_characters[i][j], replacements[i])
                }
            }
            filter.push(replaced);
            let registros = document.getElementById('registros');
            let span = document.createElement('span');
            span.innerHTML = replaced;
            registros.appendChild(span);
            let close = document.createElement('a');
            close.href='#';
            close.innerHTML = 'X';
            span.appendChild(close);
            close.addEventListener('click', removeRegistros);
            renderResults();
        }
    }
}

function removeRegistros(event){
    filter.splice(filter.indexOf(event.srcElement.parentElement.innerHTML.replace('<a href="#">X</a>', '')), 1);
    event.srcElement.parentElement.remove();
    renderResults();
}

function openModal(){
    let modal = document.getElementById('modal');
    modal.style.display = "block";
    document.addEventListener('click', closeModal);
}

function closeModal(event){
    let open_info = document.getElementById('open_info');
    let info = document.getElementById('modal-info');
    if(!info.contains(event.target) && !open_info.contains(event.target)){
        let modal = document.getElementById('modal');
        modal.style.display = "none";
        document.removeEventListener("click", closeModal);
    }
}



let orderby = document.getElementById('orderby');
orderby.addEventListener('change', changeOrder);
let filterbutton = document.getElementById('filterbutton');
let filtertextbox = document.getElementById('registro');
filtertextbox.addEventListener('keydown', addToFilter);
filterbutton.addEventListener('click', addToFilter);
let open_info = document.getElementById('open_info');
open_info.addEventListener('click', openModal);
let geral = document.getElementById('geral');
geral.addEventListener('click', load_final)
let pas1 = document.getElementById('pas1');
pas1.addEventListener('click', load_PAS1);
let pas2 = document.getElementById('pas2');
pas2.addEventListener('click', load_PAS2);
let cursos = document.getElementById('cursos');
for (let i = 0; i < todos_cursos.length; i += 1){
    let newCurso = document.createElement('option');
    newCurso.value = todos_cursos[i];
    newCurso.innerHTML = todos_cursos[i];
    cursos.appendChild(newCurso)
}
cursos.addEventListener('change', renderResults)
let pas3 = document.getElementById('pas3');
pas3.addEventListener('click', load_PAS3)

renderResults();
