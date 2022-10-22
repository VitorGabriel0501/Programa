def heartstone():
    #Declaração dos nomes dos monstros.
    p1 = input('Digite o nome do monstro 1: ')
    p2 = input('Digite o nome do monstro 2: ')

    #Pontos de vida e de ataque.
    pv1 = int(input('Diga os pontos de vida do monstro 1: '))
    pv2 = int(input('Diga os pontos de vida do monstro 2: '))

    atk1 = int(input('Declare os pontos de ataque do monstro 1: '))
    atk2 = int(input('Declare os pontos de ataque do monstro 2: '))

    #Combate.

    inicio = int(input(f'[1] - {p1} ataca {p2};\n[2] - {p2} ataca {p1}.:'))

    caso1 = pv2 - atk1
    caso2 = pv1 - atk2
    calculo1 = pv1 - atk2
    calculo2 = pv2 - atk1

    if inicio == 1:

        if caso1 <= 0 and caso2 <= 0:
            print(f'{p1} e {p2} morrem.')
        elif caso1 <= 0 and caso2 > 0:
            print(f'{p1} fica com {calculo1} pontos de vida e {p2} morre.')
        elif caso1 > 0 and caso2 > 0:
            print(f'{p1} fica com {calculo1} pontos de vida e {p2} fica com {calculo2} pontos de vida.')
        elif caso1 > 0 and caso2 <= 0:
            print(f'{p1} morre e {p2} fica com {calculo2} pontos de vida.')

    elif inicio == 2:

        if caso2 <= 0 and caso2 <= 0:
            print(f'{p1} e {p2} morrem.')
        elif caso1 <= 0 and caso2 > 0:
            print(f'{p1} fica com {calculo1} pontos de vida e {p2} morre.')
        elif caso1 > 0 and caso2 > 0:
            print(f'{p1} fica com {calculo1} pontos de vida e {p2} fica com {calculo2} pontos de vida.')
        elif caso1 > 0 and caso2 <= 0:
            print(f'{p1} morre e {p2} fica com {calculo2} pontos de vida.')


