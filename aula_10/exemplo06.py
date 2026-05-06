#CALCULA A MEDIA DE NOTAS
#NÃO SABEMOS QUANTOS ALUNOS, MAS TODOS TERÃO 4 NOTAS SEMPRE
def calcula_media(lista_notas):
    tot = sum(lista_notas)
    med = tot / len(lista_notas)
    return tot, med


contador = 1
resposta = 'S'
while True:
    print(f'Aluno {contador}')
    aluno = input('Nome do aluno: ')
    notas = []
    try:
        for i in range(4):
            nota = float(input('Informe a nota: '))
            notas.append(nota)
    except ValueError:
        print('Erro: Informe apenas valores válidos!')
        contador -=1
    except KeyboardInterrupt:
        print('O usuario interrompeu o programa.')
    else:
        total, media = calcula_media(notas)
        print('\nRESULTADO')
        print(f'Aluno: {aluno}')
        print(f'Total de pontos = {total}')
        print(f'Media de pontos = {media}')
        
    resposta = input('Deseja calcular para outro aluno? [S/N] ').upper().strip()
    #Causa de parada do loop
    if resposta != 'S':
        break
    contador +=1
print('PROGRAMA ENCERRADO!!!')