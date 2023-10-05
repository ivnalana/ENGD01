




#----------------------------------------------------------------------------

#FATO OU BOATO

ncomp = False
verify = False

abe = input('É absurdo, bizarro ou estranho (Sim/Nao)? ').strip().capitalize()

while(True):

  if abe == 'Nao' or verify is True:
    fonte = input('Tem fonte (Sim/Nao)? ').strip().capitalize()
    
    if fonte == 'Sim':
      conf = input('É confiável (Sim/Nao/Nao sei)? ').strip().capitalize()
      
      if conf == 'Sim':
        velha = input('É notícia velha (Sim/Nao)? ').strip().capitalize()
        
        if velha == 'Nao':
          ct = input('Checou tudo (Sim/Nao)? ').strip().capitalize()
          
          if ct == 'Sim':
            print('Ok pode compartilhar')
            break
            
          elif ct == 'Nao':
            ncomp = True
            break
        
        elif velha == 'Sim':
          ncomp = True
          break
      
      elif conf == 'Nao' or conf == 'Nao sei':
         ncomp = True
         break
    
    elif fonte == 'Nao':
       ncomp = True
       break
  
  elif abe == 'Sim':
     print('Melhor verificar!')
     verify = True


if ncomp:
  print('Na dúvida, NÃO compartilhe!')


        




