//tratamento de erros Try Catch Throw

function contarQuantidadeLetras(produto){
    try{
        console.log(produto.nome.length);    
    }
    catch(erro){
        console.log("Erro ao processar!\nCódigo de erro: 222")
        console.log("log do erro")
    }
    finally{//finally sempre é executado, independente da execução ser sucedida ou não
        console.log("Essa é a linha finally e sempre será executada!\n")
    }
}

var produto = {
    nom: "Notebook", //erro de nome de variável colocado propositalmente
    preco: 8000
}

contarQuantidadeLetras(produto)


//utilizando throw

try {
    if(!produto.nome)
        throw ("Não existe a variável \"nome\" em produto")
    else    
        console.log(produto.nome.length);
} 
catch (e) {
    console.log(e); // Logs the error
}
