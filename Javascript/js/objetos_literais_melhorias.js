//Maneira tradicional
/*
let nome = "Notebook"
let preco = 2000

const produto ={
    nome: nome,
    preco: preco,
    exibirProduto : function(){
        console.log(`${this.nome} = ${this.preco}`)
    }
}
produto.exibirProduto()
*/

//Utilizando melhorias do Javascript
let nome = "Notebook"
let preco = 2000

const produto ={
    nome, //ele já entende que quero pegar variável nome
    preco,
    exibirProduto(){ //não preciso mais declarar literalmente a função
        console.log(`${this.nome} = ${this.preco}`)
    }
}
produto.exibirProduto()
produto.nome = "Geladeira"
produto.categoria = "Eletrônicos" //posso criar atributos fora da classe e mostrá-los utilizando o método
produto.exibirProduto()
delete produto.nome
produto.exibirProduto()
produto.nome = "TV"

produto.exibirCategoria = function(){ //assim como também posso criar funções
    console.log(`${this.nome} = ${this.preco} / ${this.categoria}`)
}

produto.exibirCategoria()

//copia de objetos

const pro = produto //Dessa forma não se cria uma cópia, apenas o mesmo objeto com nomes diferentes (apontando para o mesmo endereço de memória)
//ex:
produto.preco = 5000
pro.preco = 1200
console.log(produto.preco)
