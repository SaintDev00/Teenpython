Precio_pan = 300

cantidad=int(input("Ingrese la cantidad de panes"))

if cantidad <0:
    print("cantidad invalida")
subtotal = cantidad*Precio_pan
descuento = 0
porcentaje = 0

if cantidad >0 and cantidad <=20:
    print(subtotal)


elif cantidad >20 and cantidad <=50:
    descuento=subtotal*0.10
    descuento_2=subtotal-porcentaje
    print("El precio es:", descuento_2)
    print(F"El descuento es: {descuento}")
    
elif cantidad >50:
    descuento=subtotal *0.20 
    descuento_1=subtotal-descuento
    print(f"El precio es: {descuento_1}")
    print(F"El descuento es: {descuento}")
