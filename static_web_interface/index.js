let notas_PAS1 = getNotasPAS1();
let filter = [];

function renderResults(){
    let table = document.getElementById('table');
    table.innerHTML = ''
    let HeadearRow = document.createElement('tr')
    let titles = ['Posição', 'Nome', 'Nota Final PAS1', 'Somatório Escores Brutos PAS1 ', 'Nota Redação PAS1', 'Nota Item Tipo D PAS1'];
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
            filter.push(registro.toLowerCase())
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



let orderby = document.getElementById('orderby');
orderby.addEventListener('change', changeOrder);
let filterbutton = document.getElementById('filterbutton');
let filtertextbox = document.getElementById('registro')
filtertextbox.addEventListener('keydown', addToFilter)
filterbutton.addEventListener('click', addToFilter)
renderResults()
