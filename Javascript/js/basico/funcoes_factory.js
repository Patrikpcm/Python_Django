//Factory - É um Design Pattern (padrão de design ou padrão de projetos)
//Padrão de projetos -> Básicamente são formas comuns de resolver problemas
//Funções Factory permitem que se retorne um objeto no retorno da função

const produto1 = {
    nome: "notebook",
    preco: 1200
}

const produto2 = {
    nome: "notebook",
    preco: 1200
}

//em vez de utilizar essa abordagem, eu utilizo uma função factory

const produtoFactory = function(nome, preco){

    //dados

    return{
        nome,
        preco,
        recuperarAvaliacoes(){
            console.log(`Avaliações para ${this.nome}`)
        }
    }
}

const produto = produtoFactory("Roteador",500);
console.log(produto);
produto.recuperarAvaliacoes();