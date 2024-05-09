const obj = document.getElementById('conteudo');
const obj2 = document.getElementById('conteudo2');
const obj3 = document.getElementById('conteudo3');

/*
Para inserir um texto no html posso usar o textContent e o innerHTML.
O textContent tem um problema pois com ele consigo adicionar apenas texto.
Já com o innerHTML eu consigo inserir também tags html.
*/
obj2.textContent = "<p>O rato roeu a roupa do rei de roma</p>"; 
obj3.innerHTML = "<p style='color:red'>O rei ficou muito brabo</p>"

/*************/

const ul = document.getElementById('itens');

const li = document.createElement('li');//método que cria um elemento dentro do html
li.setAttribute('id', 'item3');
ul.appendChild(li);//adicionando um elemento li vazio.
li.textContent = ("Gogola"); //adicionando texto ao elemento vazio criado


const li2 = document.createElement('li'); //criando elemento vazio
li2.appendChild(document.createTextNode("texto criado com createTextNode"));
li2.setAttribute('id', 'item4'); //adicionando um atributo ao elemento.
ul.appendChild(li2);//adiciondo um elemento, agora não vazio

const clonar = document.getElementById('conteudo3'); 
const clone = clonar.cloneNode(true);//clonando elementos 
console.log(clone);
console.log(clone.textContent);
document.getElementById('conteudo3').appendChild(clone);

/********criando funções pra adicionar e remover itens da lista*******/
var qtdItens = 4;

function adicionar(texto){
    qtdItens++;
    const ul = document.getElementById('itens'); //obtendo a ul de interesse
    const novoli = document.createElement('li'); //criando um novo item li
    novoli.appendChild(document.createTextNode(texto.value)); //atribuindo o texto digitado pelo usuario
    novoli.setAttribute('id','item'+qtdItens); //setando novo atributo que identifica o item nesse exemplo
    ul.appendChild(novoli); //inserindo o novo li na ul.
}

function remover(item){
    const ul = document.getElementById('itens'); //obtendo a ul de interesse
    const li = document.querySelector('#item'+item.value); //selecionando o item que desejo remover
    console.log(li.textContent);//mostrando no console o item que foi excluido
    li.remove();//removendo o item li
    qtdItens--;//diminuindo o numero de itens
    for(let i=0; i<qtdItens; i++){ //renomeando o valor dos itens para não perder a sequencia da lista
        ul.children[i].setAttribute('id', 'item'+i);
    }
}


