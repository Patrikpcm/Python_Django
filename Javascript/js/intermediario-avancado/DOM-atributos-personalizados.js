const obj = document.getElementById('itens');

console.log(obj);
console.log(obj.quantidade); //dessa forma não funciona pois quantidade não é um atributo nativo do HTML.
console.log(obj.getAttribute('quantidade'));//forma correta de recuperar atributos personalizados
obj.setAttribute('quantidade','10'); //atribuir novo valor
console.log(obj.getAttribute('quantidade'));

//utilizando a nomeclatura correta de atributos personalizados eu posso recupera-los diretamente.
console.log(obj.dataset.status); 
obj.dataset.status = "Concluído";
console.log(obj.dataset.status); 

console.log(obj.hasAttribute("quantidade"));//verificar se eu possuo o atributo no elemento.
console.log(obj.hasAttribute("mandioca"));

console.log(obj.attributes);
console.log(obj.attributes[1]);//posso acessar atributos pela posição (não consigo altera-los dessa forma)

const obj2 = document.getElementById("labelNome");
console.log(obj2);
console.log(obj2.attributes);
console.log(obj2.id);
//recuperar elementos que utilizam palavras reservadas da linguagem JS implica em erro, portanto não
//posso fazer a recuperação dos dados do for dessa forma. Receberei 'undefined'
console.log(obj2.for);
//devo realizar dessa forma, e ai sim conseguirei recuperar os dados.
console.log(obj2.htmlFor);

obj.removeAttribute("data-status");//removendo um atributo do elemento