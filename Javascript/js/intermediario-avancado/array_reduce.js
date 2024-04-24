/*
Reduce pode servir como uma função de soma total de um array ou análise de geral de
dados, como por exemplo, avaliar se todos os dados são verdadeiros ou falsos.
*/
const numeros = [2,3,5];

const funcao = function(acumulador, atual, i, arr){
    console.log("i: "+i);
    console.log("ac: "+acumulador);
    console.log("at: "+atual);
    console.log("-------\n")
    return (acumulador + atual);
}

const resultado = numeros.reduce(funcao);

console.log(resultado);


console.log("\n");


const produtos = [  {nome:"Notebook", promocao: false},
                    {nome:"Celular", promocao: false},
                    {nome:"Tablet", promocao: false},  
                    {nome:"Monitor", promocao: false} ];

const promo = produtos.map(produto => produto.promocao); //fazendo um map para extrair apenas o valor bool

const funcbool = function(acumulador, atual, i, arr){ //função que retorna se existe promoção
    return (acumulador || atual);
}

const temPromo = promo.reduce(funcbool); //uso do reduce utilizando a função funcbool

temPromo ? console.log("tem promoção") : console.log("Não tem promoção"); //resultado