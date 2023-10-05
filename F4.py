

#-------------------------------------------------------------------------------

#Exercícios a fazer

nfazer = False

print('Você tem exercícios a fazer')

ponto = input('Vale ponto (Sim/Nao)? ').strip().capitalize()

if ponto == 'Sim':
  tom = input('É para amanhã (Sim/Nao)? ').strip().capitalize()
  
  if tom == 'Sim':
    cop = input('Tem como copiar (Sim/Nao)? ').strip().capitalize()
    
    if cop == 'Nao':
      need = input('Você precisa dos pontos (Sim/Nao)? ').strip().capitalize()
      
      if need == 'Sim':
        net = input('Tem a resposta na internet (Sim/Nao)? ').strip().capitalize()
        
        if net == 'Nao':
          outro = input('Alguém pode fazer por você (Sim/Nao)? ').strip().capitalize()
          
          if outro == 'Nao':
            print('Então faça!')
          
          elif outro == 'Sim':
            nfazer = True
          
        elif net == 'Sim':
          print('Então copie!')

      elif need == 'Nao':
        nfazer = True
      
    elif cop == 'Sim':
      nfazer = True
      
  elif tom == 'Nao':
    nfazer = True
    
elif ponto == 'Nao':
  nfazer = True

if nfazer:
  print('Então não faça!')

#-------------------------------------------------------------------------------



        




