/*
Eventos de Interface de Usuário
- load (onload): A página web terminou de carregar
- unload(onunload): A página web está carregando
- error(onerror): O navegador encontra um erro
- resize(onresize): A janela do navegador foi redimensionada
- scroll(onscroll): Usuário rolou a página para cima ou para baixo
*/

function executar(){
    console.log("Executou!");
}

/*Exemplos de cada função*/
//window.addEventListener('load',executar); 
//window.addEventListener('unload',executar);
//window.addEventListener('error',executar); windo.addEventListener('unload',executar); //chamada com erro de digitação para exemplificar o erro
//window.addEventListener('resize',executar);
window.addEventListener('scroll',executar);