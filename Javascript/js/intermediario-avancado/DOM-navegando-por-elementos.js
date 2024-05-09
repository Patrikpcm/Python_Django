const lista = document.querySelector('div#itens');
console.log(lista);
console.log(lista.parentNode);
console.log(lista.parentNode.parentNode);
console.log(lista.childNodes);//contabilizando os espaços
console.log(lista.firstChild);//contabilizando os espaços
console.log(lista.lastChild);//contabilizando os espaços, por isso é exibido text no console.

const irmao = document.querySelector('div#itens');
console.log(irmao.nextSibling);
console.log(irmao.previousSibling);

console.log(lista.children); //não contabiliza os espaços.
console.log(lista.firstElementChild); // desconsidera os espaçamentos
console.log(lista.lastElementChild);// desconsidera os espaçamentos

console.log(irmao.nextElementSibling);// desconsidera os espaçamentos
console.log(irmao.previousElementSibling);// desconsidera os espaçamentos