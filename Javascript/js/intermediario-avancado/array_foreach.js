/*
Utilizando o método foreach() conseguimos percorrer um array e aplicar, por exemplo, uma função para
cada item do mesmo.

var fruta = ["maça", "laranja", "Amora"];
fruta.foreach(minhaFuncao);

function minhaFuncao(item, index){
    document.getElementById{"demo"}.innerHTML += index + ":" + item + "<br>";
}
*/ 

const lista = ["Jamilton", "Ana", "Marcela", "Pedro"];

/* exemplo de como seria
for (indice in lista){
    console.log(lista[indice])
}
*/

function percorrer (item, index, arr){
    console.log(item);
}

lista.forEach(percorrer);