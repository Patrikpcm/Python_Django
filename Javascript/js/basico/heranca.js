class Animal{
    constructor(cor, tamanho, peso){
        this.cor = cor
        this.tamanho = tamanho
        this.peso = peso
    }

    comer(){
        return ("O animal esta comendo")
    }
    dormir(){
        return ("O animal esta dormindo")
    }
}

class Cao extends Animal{
    latir(){
        return "O cão esta latindo"
    }
    correr(){
        return "O cão esta correndo"
    }
}

class Passaro extends Animal{
       
    voar(){
        return "O passaro esta voando"
    }
}

class Papagaio extends Passaro{
    //A palavra reservada Super() faz com que nao haja erro de compilação pois esse indicativo
    //diz que a classe filha não quer sobrescrever o construtor da classe mãe
    constructor(cor, tamanho, peso, bico, palavras){
        super(cor, tamanho, peso)
        this.bico = bico
        this.palavras = palavras
    }

    falar(){
        return "O papagaio esta falando"
    }

    comer(){
        //POLIMORFISMO DA FUNÇÃO COMER
        return super.comer() + " como um papagaio"
        //super.comer() são ações genéricas da classe animal + um método específico
    }
}

//main
animal = new Animal()
console.log(animal.comer())
console.log(animal.dormir())
console.log("\n")

cao = new Cao()
console.log(cao.latir())
console.log(cao.correr())
console.log("\n")

passaro = new Passaro()
console.log(passaro.voar())
console.log("\n")



papagaio = new Papagaio("verde", 30, 2, "longo-curvado", 60)
console.log(papagaio.falar())
console.log(papagaio.comer())
console.log(papagaio.cor)
console.log(papagaio.tamanho)
console.log(papagaio.peso)
console.log(papagaio.bico)
console.log(papagaio.palavras)

