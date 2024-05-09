/*
-keydown: O usuário pressiona uma tecla(qualquer tecla, até mesmo ctrl, shift, caps, etc)
-keyup: O usuário solta uma tecla
-keypress: Caracteres estão sendo inseridos
*/

function executar(){
    console.log("executou!");
}

/*Exemplos de utilização das funções */
const obj = document.getElementById('entrada');
//obj.addEventListener('keydown', executar);
//obj.addEventListener('keyup', executar);
obj.addEventListener('keypress', executar);