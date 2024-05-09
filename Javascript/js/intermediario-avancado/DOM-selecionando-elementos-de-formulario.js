
const obj = document.getElementsByName('cadastro');
console.log(obj);
console.log(obj[0]);

console.log(document.forms);//acessando formulários diretamente, sem uso de getElementsByName
console.log(document.cadastro);//acessando elementos pelo nome
console.log(document.cadastro.sexo);//acessando subelementos pelo nome

document.cadastro.nome.value = "Patrik"; //configurando um valor diretamente no value

function salvar(){
    //pré preenchendo o valores
    /*
    document.cadastro.sexo.value = "masculino";
    document.cadastro.email.value = "email@email";
    document.cadastro.nome.value = "Patrik";
    */

    //recuperando o que o usuário digitou
    let nome = document.cadastro.nome.value;
    let email = document.cadastro.email.value;
    let sexo = document.cadastro.sexo.value;
    console.log(nome);
    console.log(email);
    console.log(sexo);

    //recuperando valores pelo ID
    const obj = document.getElementById('email');
    console.log(obj.value);
}