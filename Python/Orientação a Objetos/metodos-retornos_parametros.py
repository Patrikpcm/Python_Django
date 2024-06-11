class Usuario:
    #a nomeclatura self é padrão, mas pode ser trocada por outra coisa. Como por user nesse ex
    def __init__(user, email, senha) -> None:
        user.email = email
        user.senha = senha
        user.enderecos = []

    """
    O método __str__ retorna uma string quando o objeto é chamado.
    Por exemplo, sem esse método se tentarmos dar um print na instância
    print(usuario) o retorno será a informação sobre o objeto, algo como 
    '<__main__.Usuario object at 0x7f802b5f9040>'.
    Utilizando esse método, o retorno é a string pré-definida.
    """
    def __str__(user) -> str: 
        return (f'email: {user.email}, senha: {user.senha}')

    """
    método iter faz a iteração de uma lista sem precisar apontar diretamente para ela
    caso se tenha um objeto lista na classe.
    Ex: para imprimir endereços fora da classe utilizando um for, eu deveria 
    declarar a chamada da seguinte forma:
    
    for endereco in usuario.enderecos:
        print(endereco)

    Utilizando o método __iter__:
    for endereco in usuario:
        print(endereco)

    """
    def __iter__(user):
        return user.enderecos.__iter__()

    """
    Em python não existe membros privados e publicos como em outras linguagens, o que
    existe são boas práticas definidas pela comunidade. Portanto se você deseja que 
    um método ou variável seja privado, o conceito que se utiliza é aplicar um
    underline "_" antes do nome do objeto.
    """
    def _validar(user):
        email_cadastro = 'email@email.com'
        senha_cadastro = '1234'

        if (email_cadastro == user.email) and (senha_cadastro == user.senha):
            print("Login executado!")
        else:
            print("Email ou Senha incorretos!")

    def logar(user):
        user._validar()
        print("Enviar para tela principal")

    def forca_senha(user):
        if len(user.senha) > 5:
            return True
        else:
            return False
        
    def cadastrar_endereco(user, endereco1, endereco2):
        #print(f'Endereços:\n{endereco1}\n{endereco2}')
        user.enderecos.append(endereco1)
        user.enderecos.append(endereco2)


usuario = Usuario('email@email.com', '1234')
usuario.logar()
usuario._validar() #como descrito acima, eu posso utilizar o método, mas o underline é uma indicação de que eu não deveria utiliza-lo aqui por se tratar de um método privado
if(usuario.forca_senha()): #o método pode retornar um valor
    print("Senha forte!")
else:
    print("Senha fraca!")

enderecos = ["Rodovia Gumercindo Boza","Estrada do Cerne"]
usuario.cadastrar_endereco(*enderecos) #unpacking passando uma lista

print(usuario) #possivel imprimir utilizando __str__

for endereco in usuario: #Possivel chamar a iteração diretamente por ter definido __iter__ na classe
    print(endereco)      #Caso contrário deveria ter chamado endereco in usuario.enderecos: