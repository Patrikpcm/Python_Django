/*
-focus: O elemento ganha o foco
-blur: O elemento perde o foco
*/

function executar(){
    console.log("executou!");
    //obj.focus()
}

function executarBlur(){
    console.log("executou blur!");
}

/*Exemplos de utilização das funções */
const obj = document.getElementById('entrada');
const obj2 = document.getElementById('entrada');

obj.addEventListener('focus', executar);
obj2.addEventListener('blur', executarBlur);