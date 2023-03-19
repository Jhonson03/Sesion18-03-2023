print("Bienvenido al restaurante")

print('''
      \tMenu
      1- Especialida
      2- Bebidas''')

Menu = str(input("Ingrese una opcion del menu -> ")).lower()

if Menu == "especialidad" or Menu == "1":
    print('''\tMenu De Especialidad
          1- Mar y Tierra
          2- Pupusas''')
    
    Menu2 = input("\nIngrese una opcion del menu -> ").lower()
    
    if Menu2 == "1" or Menu2 == "mar y tierra":
        print("Usted eligio el plato de mar y tierra")
        
    elif Menu2 == "2" or Menu2 == "pupusas":
        print("Usted eligio pupusas")
        
    else:
        print("La opcion no se encuentra disponible")
        
elif Menu == "bebidas" or Menu == "2":
    print('''Menu De Bebidas
          1- Cocacola
          2- Pepsi''')
    
    Menu2 = input("\nIngrese una opcion del menu -> ").lower()
    
    if Menu2 == "1" or Menu2 == "cocacola":
        print("Usted eligio la bebida cocacola")

    elif Menu2 == "2" or Menu2 == "pepsi":
        print("Usted eligio la bebida pepsi")

    else:
        print("La opcion no se encuentra disponible")
        
else:
    print("La opcion no se encuentra disponible")
    
print("Fin del programa")