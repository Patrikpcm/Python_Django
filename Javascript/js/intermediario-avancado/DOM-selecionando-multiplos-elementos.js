/* */

/*
function executar(){
    const obj = document.querySelector('li.primeiro')
    obj.innerHTML = "Preto - branco";
    obj.classList.add("preto-branco");
}

Enquanto o querySelector captura apenas o primeiro elemento encontrado na página, o querySelectorAll
captura todos. 
obs: Para melhor entendimento descomente essa função e comente a abaixo.
*/
function executar(){
    const obj = document.querySelectorAll('li.primeiro')
    obj.innerHTML = "Preto - branco";
    //para cada membro do querySelectorAll eu adiciono a classe. 
    //Esse método, diferente dos demais, possui algumas propriedades de arrays, como o forEach()
    obj.forEach(function (o){ 
                                o.classList.add("preto-branco");
                            });
        
}

/*
Isso cria uma coleção de objetos que contem div. Eles podem ser acessados pelo índice como pode ser visto
com console.log
*/
const divs = document.getElementsByTagName('div'); 
console.log(divs);
console.log(divs[0]);
console.log(divs[1]);
console.log(divs[2]);
console.log(divs[3]);

/*Essa coleção é diferente de um array, não possui as mesmas propriedades. Mas pode ser convertido em array
como mostra esse método. E dessa forma usar as propriedades existentes no método Array*/
const colecao = document.getElementsByTagName('li');
const lista = Array.from(colecao);

const funcao = function(item, i){
    console.log(item);
}
lista.forEach(funcao);

/*Aqui podemos capturar os elementos pelo nome da classe*/
const classes = document.getElementsByClassName('vermelho');
console.log(classes);

/*Capturando elementos pelo nome*/
const nomes = document.getElementsByName('nome');
console.log(nomes);
console.log(nomes[2]);
