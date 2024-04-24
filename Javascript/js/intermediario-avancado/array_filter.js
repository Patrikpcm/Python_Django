/*
Filter é uma função que retorna verdade ou falso.
*/

const usuarios = [  {nome: "Patrik", idade: 34}, 
                    {nome: "Felipe", idade: 30},
                    {nome: "Aylla", idade: 7},
                    {nome: "Caio", idade: 1}    ];

function maiorIdade(item, i, arr){
    //true ou false
    console.log(this);
    if (item.idade >= 18)
        return true; 
    else
        return false;
}

const arrMaiorIdade = usuarios.filter(maiorIdade);
console.log(usuarios);
console.log("Maiores de idade são:")
console.log(arrMaiorIdade);