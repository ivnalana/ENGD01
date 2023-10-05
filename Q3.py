

#----------------------------------------------------------------------------
#questão 3 (Lista 1)
#-----------------------------------------------------------------------------


from math import sqrt

I = 0

N = 0

while True:
    N = N + 1
    a = input('Digite o valor do coeficiente "a": ')
    try:
        a = float(a)
    except:
        print('O coeficiente precisa ser um número!!! Digite novamente.')
        continue
    if a == 0:
        print('Valor do coeficiente "a" inadequado')
        I = I + 1
        continue


    b = input('Digite o valor do coeficiente "b": ')

    try:
        b = float(

    except:

        print('O coeficiente precisa ser um número!!! Digite novamente.')
        continue

    c = input('Digite o valor do coeficiente "c": ')

    try:
        c = float(c)
    except:
        print('O coeficiente precisa ser um número!!! Digite novamente.')
        continue

    delta = (b**2 - 4*a*c)
    if delta < 0:
        print('A equacão não possui raízes reais.')

    else:
        r1 = ((-b + sqrt(delta))/2*a)
        r2 = ((-b - sqrt(delta))/2*a)

        print(f'As raízes dessa equação são {r1} e {r2}.')

    nc = input('Deseja fazer outro cálculo (Sim/Nao)? >>> ').strip().capitalize()

    if nc == 'Nao':
        break
    else:
        continue

print(f'O programa foi rodado {N} vezes e a quantidades de coeficientes "a" inadequados foram {I} vezes.')


