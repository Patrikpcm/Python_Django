class Usuario{
    constructor(){
        this.email = ""
        this.senha = ""
        this.subtotalCompra = "0"
    }

    logar(){
        let emailBD = "plg@email.com"
        let senhaBD = "1234"

        if(senhaBD == this.senha){
            return ("Senha válida")
        }
        else{
            return("Senha inválida")
        }
    }

    calcularDesconto(cupom){
        let desconto = 0

        if(cupom == "DESC20")
            desconto = 20
        else if(cupom == "FESTA10")
            desconto = 10

        return(this.subtotalCompra - desconto)
    }
}

const usuario = new Usuario()
usuario.email = "plg@email.com"
usuario.senha = "1234"

console.log(usuario.logar())

usuario.subtotalCompra = 279
console.log(usuario.calcularDesconto("DESC20"))