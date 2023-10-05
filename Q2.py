

#----------------------------------------------------------------------------
#questão 2 (Lista 1)
#-----------------------------------------------------------------------------

preços = {  'Hambúrguer' : 3.00 ,
            'Cheeseburguer' : 2.50 ,
            'Fritas' : 2.50,
            'Refrigerante' : 1.00 ,
            'Milkshake' : 3.00 }

while True:
    total = 0

    for i in preços:

        qtd = int(input(f' Informe a quantidade do item {i} >>>'))
        total = qtd*preços[i] + total

    print(f'\nA conta final foi R$ {total}')

    c = input('Deseja calcular novamente (Sim/Nao)? ').strip().capitalize()

    if c == 'Nao':
        break

