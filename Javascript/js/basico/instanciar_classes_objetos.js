/*Formas de se fazer a definição de objetos */

//Notação literal - Objeto e seus atributos
const hotel = {
    quartos: 20,
    ocupados: 10,
    piscinas: 2,

    verificarDisponibilidade: function(){
        let res = (this.quartos - this.ocupados)
        return "Disponível: " + res
    }
}

hotel.quartos = 30
hotel.ocupados = 25
//hotel['quartos'] = 40 //outra forma de criar atribuições
//hotel['ocupados'] = 30 //mas normalmente utilizamos o ponto "."
console.log(hotel.verificarDisponibilidade())
delete hotel.piscinas
console.log(hotel.piscinas)



//Notação de construtor (objeto em branco)
const hostel = new Object()
hostel.quartos = 10
hostel.ocupados = 9
hostel.verificarDisponibilidade = function(){
    let res = this.quartos - this.ocupados
    return "Disponíveis: " + res
}
console.log("\n"+hostel.verificarDisponibilidade())


//Notação com criação de classes(mais simples)
class Motel{
    
    constructor(){
        console.log("\nconstruindo o objeto")
        this.quartos = 15
        this.ocupados = 1
    }

    verificarDisponibilidade(){
        console.log("Disponíveis: " + (this.quartos - this.ocupados))
    }
}

const motel = new Motel()
motel.verificarDisponibilidade()