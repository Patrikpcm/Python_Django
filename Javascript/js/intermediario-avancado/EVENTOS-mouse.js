/*
-click: Pressiona e solta o botão do muse sobre o mesmo elemento
-dblclick: doble click sobre o mesmo elemento
-mousedown: pressiona o botão do mouse sobre um elemento
-mouseup: solta o botão do mouse sobre um elemento
-mousemove: move o mouse **
-mouseover: move o mouse sobre um elemento **
-mouseout: move o mouse para fora de um elemento **

-Os elementos com "**" não funcionam em telas touchscreen pela ausência do mouse.
-Os eventos de mouse funcionam para vários outros elementos HTML além de input e button.
*/

function executar(){
    console.log("executou!");
}

function executarDuplo(){
    console.log("duplo click!");
}

/*Exemplos de utilização das funções */
const obj = document.getElementById('botao');
//const obj2 = document.getElementById('body');

//obj.addEventListener("click", executar);
//obj2.addEventListener("dblclick", executarDuplo);
//obj.addEventListener('mousedown', executar);
//obj.addEventListener("mousemove", executar);
//obj.addEventListener("mouseover", executar);
obj.addEventListener("mouseout", executar);