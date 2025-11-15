Edad=int(input("Cuantos años tienes? "))

if Edad>=18:
    Documento=input("Tienes documento? si/no").lower()
 
    if Documento == "si":
        print("Puedes entrar")
    else:
        print("No puedes entrar por falta de documento")
else:
    print("No puedes entrar")
