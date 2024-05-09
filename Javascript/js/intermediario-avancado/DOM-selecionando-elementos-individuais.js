/* */

//const obj = document.getElementById('destaque');

const obj2 = document.querySelector('#destaque');
const obj3 = document.querySelector('li.segundo');

console.log(obj2.textContent);
console.log(obj3.textContent);

function executar(){
    const obj = document.querySelector('li.primeiro')
    obj.innerHTML = "Preto - branco";
    obj.classList.add("preto-branco");
}