"""
Decorator é um padrão de projeto que permite que eu altere o comportamento de uma função
sem necessariamente mudar o código da mesma.
"""

#Exemplo 1 de padrão decorator
def passo1(p1):
    p1 = f'{p1}'
    
    def passo2(p2):
        print( f'{p1} e {p2}' )
    
    return passo2

#posso chamar a função completa em 2 passos
funcao_p2 = passo1("Abrir uma porta")
funcao_p2('Entrar na casa\n')

#ou posso chamar de uma vez
passo1("Abrir a porta")("Entrar na casa\n")


###########################################

#Exemplo 2 de padrão decorator
def verifica_usuario_logado(p_funcao):
    def verifica():
        print("[Antes vamos verificar se o usuário está logado...]")
        retorno = p_funcao()
        print('[FIM]\n')
        return retorno
    return verifica

@verifica_usuario_logado #isso é um decorator. Ele altera o fluxo de execução
def salvar_postagem():
    print("...[executando]")
    print("Postagem criada")

@verifica_usuario_logado
def salvar_comentario():
    print("...[executando]")
    print("COMENTARIO criada")

"""
Quando chamo salvar postagem, como ela esta logo abaixo da função decorator, ela não
sera chamada diretamente. Em vez disso ela servirá como parâmetro da função DECORATOR
propriamente dita.
Nesse exemplo, quando chamo a função salvar_postagem(), ela vira o parâmetro da função
verifica_usuario_logado(p_funcao) por causa do decorator. Portanto ela é executada DEPOIS
da função verifica_usuario_logado.

Seria como se eu chamasse a função da seguinte forma:
verifica_usuario_logado(salvar_postagem)
"""
salvar_postagem()
salvar_comentario()