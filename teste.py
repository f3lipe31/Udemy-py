escolha = input ("Vertebrado ou invertebrado? ")


if escolha  == 'Vertebrado' or 'vertebrado' or '1':
        tipo = input ("Ave ou mamifero? ")
        if tipo == 'Ave':
         comida = input ("carnivoro ou onivoro? ")
         if comida == 'carnivoro':
                print ("aguia")
         elif comida == 'onivoro':
                print ("pomba")
        elif tipo == 'mamifero':
          comida = input ("onivoro ou herbivoro? ")
          if comida == 'onivoro':
                    print ("homem")
          elif comida == 'herbivoro':
                    print ("vaca")  
               
elif escolha == 'Invertebrado' or 'invertebrado' or '2':
        tipo = input ("Inseto ou anelideo? ")
        if tipo == 'Inseto':
           comida = input ("hematofago ou herbivoro? ")
        if comida == 'hematofago':
            print ("pulga")
        elif comida== 'herbivoro':
            print ("lagarta")
        elif tipo == 'anelideo':
            comida = input ("hematofago ou onivoro? ")
            if comida == 'hematofago':
                print ("sanguessuga")
            elif comida == 'onivoro':
                print ("minhoca")

       
