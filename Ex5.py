Libro = 25000

Estudiante=input("Eres estudiante? yes/no ").lower()

match Estudiante:
    case'yes':
        Myu = 25000-(25000 * 0.15)
        cupon=input("Tienes cupon? ingresa el codigo")                                      

        if cupon== "LIBRO10":                                               
            precio_final=Myu * 0.90                                                                                                                
            print(f"Tu precio es {precio_final}")                                                                                          
        else:
            print(f"Tu precio es {Myu}")                                    
    case 'no':
        print("Tu precio total es de:25000")

    case _:
        print("Por favor responder yes or no")
    
