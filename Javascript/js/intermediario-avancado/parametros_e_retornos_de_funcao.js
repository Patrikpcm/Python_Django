//parâmetros padrão

function somar(num1, num2){
    return num1+num2
}

//NaN -> Not a Number
console.log(somar(2));
console.log(isNaN(somar(2,3)));
console.log(somar(2, 4) == isNaN)
console.log(isNaN(somar(1)));
console.log(somar(2) == isNaN)