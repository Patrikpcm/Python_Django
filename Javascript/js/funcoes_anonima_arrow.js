//função convencional
function somar(a, b){
    console.log(a+b)
}

//função Anônima
const subtrair = function(a,b){
    console.log(a-b)
}

//função Arrow
const dividir = (a,b) =>console.log(a/b)


somar(1,2)
subtrair(2,2)
dividir(4,2)