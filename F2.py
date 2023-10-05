

#------------------------------------------------------------------------------

#Lógica simples para comentários

guarde = False

coment = input('O que vai comentar? ')

pmdi = input('Precisa mesmo dizer isso? (Sim/Nao): ').strip().capitalize()

if pmdi == 'Sim':
  util = input('É útil? (Sim/Nao) ').strip().capitalize()
  
  if util == 'Sim':
    ofend = input('Pode ofender alguém? (Sim/Nao): ').strip().capitalize()
    
    if ofend == 'Nao':
      palp = input('É um palpite? (Sim/Nao): ').strip().capitalize()
      
      if palp == 'Nao':
        vc = input('Você gostaria de ouvir? (Sim/Nao): ').strip().capitalize()
        
        if vc == 'Sim':
          print('Então comente.')
        
        elif vc == 'Nao':
          guarde = True
        
      elif palp == 'Sim':
        guarde = True
    
    elif ofend == 'Sim':
      guarde = True
  
  elif util == 'Nao':
    guarde = True
  
elif pmdi == 'Nao':
  guarde = True

if guarde:
  print('Guarde pra você!')






