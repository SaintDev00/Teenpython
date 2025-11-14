chocolate=4000
vainilla=3500
topping=1000

Helado=input("Que sabor de helado desea? \n")

match Helado:
   
    case'chocolate':
        result = chocolate + topping
   
    case'vainilla':
        result = vainilla + topping
   
    case _:
        result = "Unknown answer choose one of the two flavours..."


print(result)
    


        
