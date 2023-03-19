print("Bienvenido al programa")

Pais1 = str("ESTADOS UNIDOS")
Pais2 = str("MEXICO")
Pais3 = str("NORUEGA, Noruego")
Pais4 = str("DINAMARCA, Danesa")
Pais5 = str("ARGERTINA, Argentino")
Pais6 = str("HONDURAS, Hondureño")
Pais7 = str("INGLATERRA, Ingles")
Pais8 = str("INDIA, India")
Pais9 = str("ALEMANIA, Aleman")
Pais10 = str("COLOMBIA, COLOMBIANO")

Esp1 = "canino"
Esp2 = "felino"
Esp3 = "mamífero"
Esp4 = "roedor"

Usuario = input("Ingrese su nombre -> ")

Menu1 = input('''
             \tMenu
             1- Humanos
             2- Animales
             
             Elija una opcion del menu -> ''').lower()

if Menu1 == 'humanos' or Menu1 == '1':
    Menu2 = input(f'''
                  \tMenu De Paises
                  1- {Pais1}
                  2- {Pais2}
                  3- {Pais3}
                  4- {Pais4}
                  5- {Pais5}
                  6- {Pais6}
                  7- {Pais7}
                  8- {Pais8}
                  9- {Pais9}
                  10- {Pais10}
                  
                  Ingrese una opcion del menu -> ''').upper()
    
    if Menu2 == Pais1 or Menu2 == '1':
        print(f"{Usuario} usted es de {Pais1} el gentilicio de su pais es Americano")
    
    elif Menu2 == Pais2 or Menu2 == '2':
        print(f"{Usuario} usted es de {Pais2} el gentilicio de su pais es Mexicano")
        
    else:
        print("La opcion no esta disponible")
        
elif Menu1 == "animales" or Menu1 == "2":
    Menu2 = input(f'''
                  \tMenu de Especies
                  1- {Esp1}
                  2- {Esp2}
                  3- {Esp3}
                  4- {Esp4}
                   
                  Ingrese una opcion del menu -> ''').lower()
    
    if Menu2 == Esp1 or Menu2 == '1':
        print(f"{Usuario} usted eligio la especie {Esp1}  los animales que se encuentran son perros, lobos, etc")

    elif Menu2 == Esp2 or Menu2 == '2':
        print(f"{Usuario} usted eligio la especie {Esp2} los animales que se encuentran son gatos, tigres, etc")
    else:
        print("La opcion no esta disponible")
else:
    print("La opcion no esta disponible")

print("Fin del programa")