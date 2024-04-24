/*
console.log(typeof []);
console.log(typeof new Array);
*/

//2 formas de declarar array, as duas funcionam igual
const nomes = ["Patrik", "Felipe"];
const frutas = new Array("Morango", "Banana");

console.log(frutas[0]);
frutas.push("Abacaxi"); //inserir um item no array
console.log(frutas);
delete frutas[0];//deletar um item do array, mas deixa espaços vazios no array
console.log(frutas);
console.log(frutas.length); //tamanho
frutas.sort(); //ordenar
console.log(frutas);
let fruta = frutas.pop();//remove o último elemento de um array e o retorna, caso necessite
console.log(frutas);
fruta = frutas.shift(); //remove o primeiro elemento do array e o retorna, caso necessite

const estados = ["Rio Grande", "Santa Catarina", "Paraná", "São Paulo", "Minas Gerais", "Rio de Janeiro"];
let novo = estados.splice(0,2); //remove itens do array, iniciando de uma posição + quantidade de itens
console.log(estados);
novo = estados.splice(0,1, "substituido") //também pode ser usado para substituir itens num array
console.log(estados);
novo = estados.slice(1,3);//cortar itens do array. Criar um novo array
console.log(novo);
let texto = estados.join();//converte o array em string
console.log(texto);
let array = texto.split(",")//converte texto em array
console.log(array);