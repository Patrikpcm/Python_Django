//Funções construtoras
class Produto{
}

const produto = new Produto();
console.log(typeof Produto);
console.log(typeof produto);
console.log(typeof 3);
console.log(typeof "teste");

console.log("\n\n");


const Hotel = function(){
    this.nome = "Hotel 5";
    this.quantidadeSuites = 30;
    let suitesOcupadas = 10; //criando a variável usando let deixamos no escopo da função, dessa forma
                             //o usuário não pode modificar a variável sem utilizar os métodos da função.

    this.reservar = function(){
        if (suitesOcupadas < this.quantidadeSuites){
            suitesOcupadas++;
            console.log("ocupadas: " + suitesOcupadas)
        }
        else   
            console.log("Hotel lotado.");
    }
}

const hotel = new Hotel();
hotel.reservar();
hotel.reservar();
hotel.reservar();
hotel.reservar();
hotel.suitesOcupadas = 2;
console.log(hotel.suitesOcupadas);
hotel.reservar();
