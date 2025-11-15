tecnica = float(input("Nota técnica (0.0-5.0): "))

logica = float(input("Nota lógica (0.0-5.0): "))

if tecnica < 0 or tecnica > 5 or logica < 0 or logica > 5:
    print("Una o ambas son notas invalidas")

else:
        nota_final= (tecnica*0.7) + (logica*0.3)

        if nota_final >=3:
              print("Aprobado")
        elif nota_final >=2:
            print("Revisión")
        else:
              print("Reprobado")
