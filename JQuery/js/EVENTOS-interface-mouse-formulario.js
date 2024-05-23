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
//FOCUS, BLUR e CHANGE
$(function(){ //chamando com método ready
    $('[name=entrada]').on('change', function(){
        //focus - objeto ganha o foco
        //blur - objeto perde o foco
        //change - só é chamado quando algo no objeto é modificado    
        console.log('change');
    });
});

//SUBMIT
$(function(){ //chamando com método ready
    $('[name=formulario]').on('submit', function(e){
        //submit
        //preventDefault() não envia o formulário e recarrega a página.
        //Serve para poder realizar algumas validações antes do envio.
        e.preventDefault(); 
        console.log('submit');
    });
});

//TECLADO -  input, keydown, keyup, keypress
$(function(){ //chamando com método ready
    $('[name=entrada]').on('keypress', function(e){
        //console.log('input');
        //console.log('keydown'); //Qualquer tecla pressionada
        //console.log('keyup');
        console.log('keypress' + ' ' + e.key); //Qualquer tecla de caracteres pressionada
    });
});
*/

//CAPTURANDO DADOS PREENCHIDOS NO FORMULÁRIO
$(function(){ 
    $('[name=salvar').on('click', function(e){
        e.preventDefault();
        let nome = $('[name=entrada]').val();
        let sexo = $('[name=selecao]').val();
        let idade = $('[name=idade]:checked').val(); //seleciona o item marcado. Caso contrário pegara o primeiro item
        let selecao = $('[name=termo]:checked').val();
        console.log(`Nome: ${nome}, Sexo: ${sexo}, Idade: ${idade}, Seleção: ${selecao}`);
    });
});