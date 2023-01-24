let notas_PAS1 = getNotasPAS1();
let filter = [];

function renderResults(){
    let table = document.getElementById('table');
    table.innerHTML = ''
    let HeadearRow = document.createElement('tr')
    let titles = ['Posição', 'Nome', '<abbr title="Somatório escores brutos + Redação + item tipo D">Nota Final</abbr>', 'Somatório Escores Brutos', 'Nota Redação', 'Nota Item Tipo D'];
    for (let t = 0; t < titles.length; t++){
        let NewHeader = document.createElement('th');
        NewHeader.innerHTML = titles[t];
        HeadearRow.appendChild(NewHeader);
    }
    table.appendChild(HeadearRow)
    if(filter.length != 0){
        for(let i = 0; i < notas_PAS1.length; i++){
            let c = 0;
            if(filter.indexOf(notas_PAS1[i][0].toLowerCase().trim()) != -1){
                c++;
                let newRow = document.createElement('tr')
                table.appendChild(newRow)
                for(let j = 0; j <= notas_PAS1[i].length; j++){
                    let newTd = document.createElement('td');
                    if(j == 0){
                        newTd.innerHTML = i + 1;
                    }else{
                        newTd.innerHTML = notas_PAS1[i][j - 1];
                    }
                    newRow.appendChild(newTd);
                }
            }
            if (c == filter.length){
                break
            }
        } 
    }else{
        for(let i = 0; i < notas_PAS1.length; i++){
            let newRow = document.createElement('tr')
            table.appendChild(newRow)
            for(let j = 0; j <= notas_PAS1[i].length; j++){
                let newTd = document.createElement('td');
                if(j == 0){
                    newTd.innerHTML = i + 1;
                }else{
                    newTd.innerHTML = notas_PAS1[i][j - 1];
                }
                newRow.appendChild(newTd);
            }
        }
    }
}

function changeOrder(){
    let element = document.getElementById('orderby');
    let order = element.value;
    if (order < 2 || order > 4){
        notas_PAS1 = getNotasPAS1()
    }else{
        notas_PAS1.sort(function(a, b){
            if(b[order] == a[order]){
                return b[1] - a[1]
            }else{
                return b[order] - a[order]
            }
        })
    }
    renderResults()
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
            filter.push(replaced)
            let registros = document.getElementById('registros')
            let span = document.createElement('span')
            span.innerHTML = registro
            registros.appendChild(span)
            let close = document.createElement('a')
            close.href='#'
            close.innerHTML = 'X'
            span.appendChild(close)
            close.addEventListener('click', removeRegistros)
            renderResults()
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
    let open_info = document.getElementById('open_info')
    let info = document.getElementById('modal-info');
    if(!info.contains(event.target) && !open_info.contains(event.target)){
        let modal = document.getElementById('modal');
        modal.style.display = "none";
        document.removeEventListener("click", closeModal)
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
renderResults()
