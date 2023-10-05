#VOCE DEVE ME LIGAR?

print ('O quão bem nos conhecemos?\n')

a = "Somos parentes muito próximos"

b = "Amigos de longa data"

c = "Vizinhos"

d = "Te acho bonito"

nligue = False

quem = input(f'Digite {a}, {b}, {c} ou {d} \n >>>').strip().capitalize()

if quem == a or quem == b:
  
  print ('\nVocê tem algo importante a dizer ou só quem conversar?')
  
  assunto = input('Digite "É importante!" ou "Só conversar" \n  >>>').strip().capitalize()
  
  if assunto == 'É importante!':
    
    print('\nIsso pode ser discutido via WhatsApp ou email?')
  
    outro = input('Digite "Não!" ou "Acho que sim" \n >>>').strip().capitalize()

    if outro == 'Não!':
      
      print('\nÉ uma emergência?')
      
      e = input('\nDigite "Sim!" ou "Não..." \n >>> ').strip().capitalize()

      if e == 'Sim!':
        
        print('\nLigue para 190')
        
      elif e == 'Não...':

        nligue = True
        
    elif outro == 'Acho que sim':

      nligue = True 
        
  elif assunto == 'Só conversar':

    nligue = True 
  
elif quem == c or quem == d:
  
  nligue = True
  
  

if nligue:
  
  print('\nNão me ligue!')






