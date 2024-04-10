let nomes =[
            "Helena",
            "Helena",
            "Alice",
            "Laura",
            "Maria Alice",
            "Cecília",
            "Maitê",
            "Liz",
            "Aurora",
            "Antonella",
            "Heloísa",      
            "Maria Cecília",
            "Maria Clara",
            "Manuela",
            "Maya",
            "Sophia",
            "Valentina"
]

function carregarNomes(){
    let itensLista = ''
    
    for(indice in nomes){
        let nome = nomes[indice]
        itensLista += `<li class="list-group-item">${nome}</li>` //Utilizando crase cria-se um template stream.        
    }
    document.getElementById('lista').innerHTML = itensLista
}

function pesquisaNome(){
    let nomePesquisa = document.getElementById('campoNome').value
    let itemLista = ''

    for(indice in nomes){
        if(nomePesquisa == nomes[indice]){
            itemLista += `<li class="list-group-item">${nomes[indice]}</li>`
            document.getElementById('lista').innerHTML = itemLista
        }
    }

    if (itemLista == '')
        document.getElementById('lista').innerHTML = "Nome não encontrado"

}