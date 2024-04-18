//Encapsulamento, modificadores de acesso e getters e setters

class ContaBancaria{
    constructor(){             //javascript não possui operadores de visibilidade private, public, protected
        this._numeroConta = 0  //mas existe uma convensão de boas práticas que diz que se colocar
        this._saldo = 0         // um underline antes da variável, ela não deve ser modificada diretamente
    }

    get saldo(){
        return this._saldo
    }
    
    set saldo(valor){
        this._saldo = valor
    }

    get numeroConta(){
        return this._numeroConta
    }

    set numeroConta(numero){
        if(numero > 0){
            this._numeroConta = numero
        }
    }
}

const conta = new ContaBancaria()
//conta.numeroConta(5001) //não se atribui dessa forma, isso gerará erro de compilação
conta.numeroConta = 5001 //O javascript consegue entender de forma autonoma que deve utilizar o set
console.log(conta.numeroConta)
conta.saldo = 500
console.log(conta.saldo)
