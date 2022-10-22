def q1():
    x = float(input('digite um valor para x: '))
    y = float(input('digite um valor para y: '))

    if x > y:
        print(f'o número {x} é maior que o número {y}')
    elif x < y:
        print(f'o número {y} é maior que o número {x}')
    else:
        print('ambos os números são iguais')

def q2():
    x = int(input('digite um número: '))

    if x % 2 == 0:
        print(f'o núemero {x} é par')
    else:
        print(f'o núemro {x} é ímpar')

def q3():
    A = int(input('Digite o primeiro valor: '))
    B = int(input('Digite o segundo valor: '))

    if B % A == 0 or A % B == 0:
        print(f'{A} é múltiplo de {B}')
    elif B % A == 1 or A % B == 1:
        print(f'{A} não é múltiplo de {B}')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

if (n1 >= 0 and n1 <= 10) and (n2 >= 0 and n2 <= 10) and (n3 >= 0 and n3 <= 10):
    media = (n1 + n2 + n3)/3
    print(f'{media}')
else:
    print('O valor não pode ser calculado!')