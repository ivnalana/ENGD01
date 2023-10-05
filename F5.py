
#-------------------------------------------------------------------------------

#Solucionador de problemas

noproblem = False

bag = input('A bagaça funciona (Sim/Nao)? ').strip().capitalize()

if bag == 'Nao':
  broke = input('Você quem quebrou (Sim/Nao)? ').strip().capitalize()
  
  if broke == 'Sim':
    print('Seu imbecil')
    know = input('Alguém sabe que foi você (Sim/Nao)? ').strip().capitalize()
    
    if know == 'Sim':
      print('SE FERROU!!')
      outro = input('Dá pra jogar a culpa em alguém (Sim/Nao)? ').strip().capitalize()
      
      if outro == 'Sim':
        noproblem = True
      
      elif outro == 'Nao':
        print('SE FERROU!!')
          
    elif know == 'Nao':
      print('Esconda')
      noproblem = True

  elif broke == 'Nao':
    culpar = input('Alguém pode te culpar (Sim/Nao)? ').strip().capitalize()
    if culpar == 'Sim':
      print('SE FERROU!!')
    elif culpar == 'Nao':
      print('Se deu bem!')
      noproblem = True

elif bag == 'Sim':
  print('Nem rela')
  noproblem = True

if noproblem:
  print('SEM PROBLEMAS')

        




