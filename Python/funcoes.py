
def calcularMedia(a, b, c):
    media = (a + b + c) / 3
    return media

print(f'A média é: {calcularMedia(2,4,7)}\n')

#############################################
alunos = [
    {'nome':'Patrik', 'notas':[8,8,9]},
    {'nome':'Sabrina', 'notas':[9,9,10]},
    {'nome':'Luiz', 'notas':[7,8,9]},
    {'nome':'Josane', 'notas':[6,7,10]},
]

def calculaAlunos(lista):
    for aluno in lista:
        media = 0
        for nota in aluno['notas']:
            media += nota
        media = media / len(aluno['notas'])
        print(f"A média do aluno {aluno['nome']} é {media}")

calculaAlunos(alunos)