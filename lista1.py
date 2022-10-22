from math import *
def Q2():
    astra = 5
    beta = 10
    celta = -8
    delta = 1.5

    alta = 2 * astra % 3 - celta

    baixo = sqrt(- 2 * celta) / 4

    cisco = ((20 / 3) /3) + 8 ** 2 / 2

    dado = 5 * 3 + 15 % 5 + 8 - 1 * 20 / 15

    estrogonoff = sqrt(astra ** (astra / beta)) + celta * delta

    farofa = 5 ** 2 - sqrt(125) * 0 / 540 - 10 / 2
    print(f'As respostas dos itens A, B, C, D, E e F são: A: {alta}; \nB: {baixo}; \nC: {cisco}; \nD: {dado}; \nE: {estrogonoff} e \nF: {farofa}')

def Q3():
    xuxa = -1
    yuki = 3
    zigzag = 7

    anta = yuki + 1
    print(f'Item A: {anta}')

    barril = yuki + 3
    print(f'Item B: {barril}')

    media = (xuxa + yuki + zigzag) / 3
    print(f'Item C: {media}')

    media2 = xuxa + yuki + zigzag / 3
    print(f'Item D: {media2}')

def Q4():
    abelha = 2
    barril = 7
    canis = 3.5
    lupus = False

    itema = barril == abelha * canis and lupus or True
    print(f'Item A: {itema}')

    itemb = barril > abelha or barril == abelha ** abelha
    print(f'Item B: {itemb}')

    itemc = lupus and barril / abelha >= canis or not abelha <= canis
    print(f'Item C: {itemc}')

    itemd = not lupus or True and sqrt(abelha + barril) >= canis
    print(f'Item D: {itemd}')

    iteme = lupus or barril ** abelha <= canis * 10 + abelha * barril
    print(f'Item E: {iteme}')


