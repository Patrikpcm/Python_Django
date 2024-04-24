/*
Map é parecido com o método forEach().
A diferença é que enquanto o forEach foi feito para ser uma alternativa ao loop for,
o map foi feito para fazemos operação de transformação/alteração nos itens de um array
e ao final dessas operações ter uma lista nova com a mesma quantidade de itens da lista base.
*/

const pessoas = ["Patrik", "Luiz", "Felipe", "Caio"];

let funcao = function(item, indice, arr){
    return "Olá " + item
}

const novoArray = pessoas.map(funcao)
console.log(novoArray)


function converteDollarReal(item, indice, arr){
    console.log (item);
    item.moeda = "R$";
    item.preco = item.preco*5;
    return item;
}

const produtosDollar =[{produto: "Notebook", preco: 1200, moeda: "$"}, {produto: "Celular", preco: 800, moeda: "$"}];
const produtosReal = produtosDollar.map(converteDollarReal);
console.log(produtosReal);