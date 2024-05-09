function executar(){
    console.log("executou botão!"); //tipo 1. chamada clássica com a função.
}

function executar2(){
    console.log("executou2!"); //função utilizada para exemplificar a chamada de mais de uma função
}

function executar3(){
    console.log("executou body!"); //função utilizada para exemplificar a chamada de mais de uma função
}

function executar4(){
    console.log("executou o EventListener e o mesmo será excluído!"); //função utilizada para exemplificar a chamada de mais de uma função
    botao5.removeEventListener('click', executar4);
}

const botao = document.getElementById('botao');
botao.onclick = executar; //abordagem tipo 2. Utilizando a chamada onclick no cód. JS usando ID

const botao2 = document.querySelector('[botao-acao]');
botao2.onclick = executar; //abordagem tipo 2. Chamando onclick com atributos personalizados (Gmail usa muito)

/*
Abordagem tipo 3 - Abordagem mais aconselhada de ser utilizada. Vários grandes sites fazem dessa maneira
ex. de chamada: elemento.addEventListener('evento',nomeDaFunção, booleano)
*/
const botao3 = document.querySelector('[botao-acao2');
botao3.addEventListener('click', executar);
//botao3.addEventListener('click', function(){executar(), executar2()}); //chamada com função anônima
                                                        //dessa forma também conseguimos executar 2 ou mais funções simultâneamente


/*ORDEM DE RECEBIMENTO DAS FUNÇÕES DO LISTENER(FLUXO) - PARÂMETRO BOOLEANO*/

const botao4 = document.querySelector('[botao-acao3]');
const body = document.querySelector('body'); //ouvindo o click no body também

botao4.addEventListener('click', executar,false);
body.addEventListener('click', executar3,false)

//false e false = fluxo de dentro pra fora. Primeiro botão, depois body.
//true e true = fluxo invertido, de fora pra dentro. primeiro body, depois botão
//outras combinações, executa primeiro quem estiver como true

/*também posso remover o EventListener para ele não executar mais de uma vez*/

const botao5 = document.querySelector('[botao-acao4]')
botao5.addEventListener('click', executar4);