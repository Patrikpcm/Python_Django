/* 
        Eventos:
        - Interface:    focus, blur, change
        - Teclado:      input, keydown, keyup, keypress
        - Mouse:        click, dbclick, mouseup, mousedown, mouseover, mousemove, mouseout, hover
        - Formulário:   submit, select, change
        - Documento:    ready, load, unload
        - Navegador:    error, resize, scroll
*/
    
/*
EVENTOS DE DOCUMENTO - READY, LOAD, UNLOAD

READY - A ação só é executada depois que a árvore DOM for montada.
Isso não quer dizer que a página esta 100% carregada, as vezes podem existir
coisas ainda carregando, porém, ela esta carregada ao ponto do JS poder trabalhar.
*/
$(document).ready(function(){ 
    $('[acao-clique').on('click', function(){
        $('h1').addClass('destaque');
        console.log('clique');
    });
});
/*
Assim como posso simplificar o método jQuery() com $(), posso simplicar o READY
escrevendo a chamada com uma função, da seguinte maneira:

$(function(){ 
    $('[acao-clique').on('click', function(){
        $('h1').addClass('destaque');
        console.log('clique');
    });
});
*/

/*
LOAD - método é chamado somente quando a página esta 100% carregada.
*/
/*$(window).load(function()){} essa maneira de chamar o método foi depreciada.
Agora utiliza-se o on().*/
$(window).on('load', function(){ //load para quando a pagina esta carregada
    console.log('load completo');
});

$(window).on('unload', function(){ //unload é para quando a página esta carregando.
    console.log('unload');
});

/*EVENTOS DE NAVEGADOR - ERROR, RESIZE, SCROLL*/
$(window).on('resize', function(){
    console.log('resize');
});

$(window).on('error', function(){
    console.log('error');   //adicionar um erro na chamada da função seguinte para visulizar
                            // o efeito. Rrocar window por windo
});                        
$(window).on('error', function(){ //windo
    console.log('error');   
});

$(window).on('scroll', function(){ //windo
    console.log('scroll');   
});