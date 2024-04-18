//Pilar 1 - Abstração

/* Modelo, Entidade, Identidade, Características e Ações */

class Carro{ //isso é um modelo/classe
    constructor(){
        //características
        this.marca = "Volkswagen", 
        this.modelo = "Voyage", 
        this.cor = "Verde Pinus",
        this.placa = "ABC-1B34"
    }
    ligar(){
        return "Carro esta ligado"
    }
}

//carro é uma identidade (instância) do objeto/Entidade Carro
const carro = new Carro() //identidade
carro.modelo = "Golf"
console.log(carro.modelo)

const carro2 = new Carro()
carro2.cor = "Preto"
console.log(carro2.ligar())


//loja virtual
class Produto{
    constructor(){
        //roupas
        this.tamanho = "M",
        this.cor = "Azul",
        this.preco = "45,90",

        //eletronicos
        this.altura = "50cm",
        this.largura = "30cm",
        this.voltagem = "110v"
    }
}