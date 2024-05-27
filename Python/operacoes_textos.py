texto = "carro"
print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print(texto[4])
print("-----------")
print(texto[-5])
print(texto[-4])
print(texto[-3])
print(texto[-2])
print(texto[-1])
print("-----------")
print(texto[:3])
print(texto[1:5])
print("-----------")
print(texto[::1]) #pegando caracteres de 1 a 1
print(texto[::2]) #pegando caracteres a cada 2 
print(texto[::3]) #pegando caracteres a cada 3

print("-----------")

frase = "Meu nome é 'Patrik'" #Utilizando  aspas simples na impressao
frase2 = 'Meu nome é "Patrik"' #utilizando aspas duplas na impressao
frase3 = "Meu nome é \"Robo\"" #imprimindo caracteres especiais com \
print(frase)
print(frase2)
print(frase3)

frase4 =    "Olá," \
            " como você" \
            " está?" \
            " ...\n" #quebrando o texto mas sem adicionar linhas
print(frase4)
#outra abordagem para escrever uma quantidade maior de texto seria
frase5 = """ inclusive essa linha como esta...
O rato
roeu
a roupa
do rei
de roma
        ...inclusive essa linha."""
print(frase5)

frase6 = "O rato roeu \n a roupa do rei de Roma" #pulando uma linha
print(frase6)

print("-----------")

frase = "Meu nome é Patrik"
print("patrik" in frase) #verificando se existe uma palavra ou caractere na frase
print("Patrik" in frase)
print("Patrik" not in frase)
print("m" in frase)
print("Pedro" not in frase)
print(len(frase))
print(frase.lower()) #todas as letras minúsculas
print(frase.upper()) #todas as letras maiúsculas
print(frase) #a frase original não é alterada

print("-----------")

print(dir(str)) #visualizar todos os métodos que podem ser aplicados em strings
print(frase.split())
frase2 = "Patrik;34;Campo Magro;Brasil;"
print(frase2.split(";"))