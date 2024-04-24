function processar(callbackSucesso, callbackErro){
    /*
    ações que podem demorar
    */

    let resultadoProcessamento = false; //false
    if (resultadoProcessamento){
        callbackSucesso()
    }else{
        callbackErro()
    }
}

const salvarResultado = function(){
    /*
    ações
    */
   console.log("salvar resultado");
}

const erro = function(){
    /*
    ações
    */
    console.log("erro");
}

processar(salvarResultado, erro);