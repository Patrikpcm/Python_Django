/*
- input:    Valor de qualquer elemento <input> mudou.
- change:   Valor em uma caixa de seleção ou botão de rádio mudou.
- submit:   Usuário envia um formulário (usando botão ou tecla).
- reset:    Usuário clica em um botão reset (pouco usado atualmente).
- cut:      Usuário "recorta" o conteúdo de um campo de formulário.
- copy:     Usuário "copia" o conteúdo de um campo de formulário.
- paste:    Usuário "cola" o conteúdo de um campo de formulário.
- select:   Usuário "seleciona" um texto em um campo de formulário.
*/

function executar(){
    console.log("Executou!");
}

function submit(event){
    //event.preventDefault(); //esse comando evita o compartamento padrão de enviar os dados da página. 
                            //Dessa forma conseguimos ver o que esta acontecendo.
    if(entrada.value == ""){
        console.log("Digite um nome");
        event.preventDefault();
    }
    console.log("Executou submit!");
    console.log(event);
   
}

const form = document.formulario;
const entrada = form.entrada;
entrada.addEventListener('input', executar);
//entrada.addEventListener('cut', executar);
//entrada.addEventListener('copy', executar);
//entrada.addEventListener('paste', executar);
//entrada.addEventListener('select', executar);

const selecao = form.selecao;
selecao.addEventListener('change', executar);

const radio = form.radio;
//console.log(radio.length);
radio[0].addEventListener('change',executar);
radio[1].addEventListener('change',executar);

const checkbox = form.checkbox;
checkbox.addEventListener('change', executar);

/*eventos de submit e reset são aplicados diretamente ao formulario*/

form.addEventListener('submit', submit);
form.addEventListener('reset', executar);