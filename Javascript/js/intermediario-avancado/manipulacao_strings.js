let nome = "Gogola"

console.log(nome.length);
console.log("Gogola".length);
/*
Em javascript, quando criamos uma string(texto), ela se torna um objeto com atributos já estabelecidos.
*/
console.log(nome.length);
console.log(nome.charAt(2));
nome = "Carro do Gogola"
let n  = nome.replace("Carro","Aviao"); //replace não afeta a string original
console.log(nome);
console.log(n);
let frase = "O sucesso é ir de fracasso em fracasso sem perder o entusiasmo.";
console.log(frase.substring(0,11));
console.log(frase.substring(0,11) + "...");

nome = "Patrik-Gogola";
let resultado = nome.split("-");
console.log(resultado);
console.log(resultado[0]);
console.log(resultado[1]);

console.log(nome.toUpperCase());
console.log(nome.toLocaleLowerCase());
console.log(nome); //não altera o valor original

nome = "Ronaldinho Gaucho      ";
console.log(nome);
console.log(nome.trim(" ")); //trim remove espaços desnecessários

let a = "Olá";
let b = "Patrik";
let c = "Gogola";
a = a.concat(" ",b," ",c);
console.log(a);

//existem diversas outras funções nativas pra manipulaçao de strings, para mais olhar a documentação