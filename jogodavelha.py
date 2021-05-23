tabuleiro = []

for i in range(0, 3):
    lugares = []
    for j in range(0, 3):
        lugares.append('()')
    tabuleiro.append(lugares)

def mostrar_tabuleiro(): #Não consegui deixar o tabuleiro bonito e elegante, mas o jogo funciona perfeitamente
    for l, linhas in enumerate(tabuleiro):
        print(f'{linhas}')
    print('-' * 30)

def mensagem_inicial():
    print('-' * 30)
    print('Jogo da Velha!!')
    print('-' * 30)

def jogadores_jogadas():
    escolha = input('Jogador 1, Você Quer Jogar com "X" ou "O"?: ')
    print('-' * 30)
    while escolha not in 'xXoO' or len(escolha) == 0:
        print('Você Só Pode Escolher Entre "X" ou "O"')
        print('-' * 30)
        escolha = input('Jogador 1, Você Quer Jogar com "X" ou "O"?: ')
    if escolha in 'xX':
        jogador1 = 'X'
        jogador2 = 'O'
        print(f'Jogador 1, Você Jogará com "{jogador1}"\nJogador 2, Você Jogará com "{jogador2}"')
        print('-' * 30)
        print('Jogador 1, Você Começa!')
        print()
    else:
        jogador1 = 'O'
        jogador2 = 'X'
        print(f'Jogador 1, Você Jogará com "{jogador1}"\nJogador 2, Você Jogará com "{jogador2}"')
        print('-' * 30)
        print('Jogador 1, Você Começa!')
        print()


    mostrar_tabuleiro()
    lista_jogadas = []
    jogo = True
    while jogo:
        while True:
            try:
                jog1 = int(input('Em Qual Posição Você Deseja Jogar Jogador 1? (Informe Posições de 0 a 8): '))
                while jog1 in lista_jogadas or jog1 < 0 or jog1 > 8:
                    print('Posição Já Ocupada! Ou Posição Não Existente')
                    jog1 = int(input('Em Qual Posição Você Deseja Jogar Jogador 1? (Informe Posições de 0 a 8): '))
            except ValueError:
                print('Digite Somente Números!')
            else:
                lista_jogadas.append(jog1)
                if 0 <= jog1 <= 2:
                    tabuleiro[0][jog1] = jogador1
                    mostrar_tabuleiro()
                if 2 < jog1 <= 5:
                    tabuleiro[1][jog1 - 3] = jogador1
                    mostrar_tabuleiro()
                if 5 < jog1 <= 8:
                    tabuleiro[2][jog1 - 6] = jogador1
                    mostrar_tabuleiro()
                if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == jogador1 or \
                    tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == jogador1 or \
                    tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == jogador1 or \
                    tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == jogador1 or \
                    tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == jogador1 or \
                    tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == jogador1 or \
                    tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador1 or \
                    tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador1:
                    print('Parabéns Jogador 1! Você Ganhou!')
                    mostrar_tabuleiro()
                    exit()

                if len(lista_jogadas) == 9:
                    print('Empate!!')
                    exit()

                while True:
                    try:
                        jog2 = int(input('Em Qual Posição Você Deseja Jogar Jogador 2? (Informe Posições de 0 a 8): '))
                        while jog2 in lista_jogadas or jog2 < 0 or jog2 > 8:
                            print('Posição Já Ocupada! Ou Posição Não Existente')
                            jog2 = int(input('Em Qual Posição Você Deseja Jogar Jogador 2? (Informe Posições de 0 a 8): '))
                    except ValueError:
                        print('Digite Somente Números!')
                    else:
                        lista_jogadas.append(jog2)
                        if 0 <= jog2 <= 2:
                            tabuleiro[0][jog2] = jogador2
                            mostrar_tabuleiro()
                        if 2 < jog2 <= 5:
                            tabuleiro[1][jog2 - 3] = jogador2
                            mostrar_tabuleiro()
                        if 5 < jog2 <= 8:
                            tabuleiro[2][jog2 - 6] = jogador2
                            mostrar_tabuleiro()
                        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == jogador2 or \
                            tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == jogador2 or \
                            tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == jogador2 or \
                            tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == jogador2 or \
                            tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == jogador2 or \
                            tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == jogador2 or \
                            tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador2 or \
                            tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador2:
                            print('Parabéns Jogador 2! Você Ganhou!')
                            mostrar_tabuleiro()
                            exit()
                        break


mensagem_inicial()
jogadores_jogadas()




