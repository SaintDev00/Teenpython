CU=2000
 
Total=int(input("Cuantas unidades compro?"))

subtotal = CU * Total

if Total >=30:
    precio_final=subtotal * 0.85
    print(f"Tu precio final es: {precio_final:.2f}")

elif Total >=10:
    precio_final=subtotal * 0.95
    print(f"Tu precio final es: {precio_final:.2f}")

else:
    precio_final = subtotal
    print(f"Tu precio es:{subtotal:.2f}")

if precio_final < 50000:
    precio_final=precio_final+5000
    print(f"Tu precio con envio es: {precio_final:.2f}")

else:
    print(f"Tu precio final es: {precio_final:.2f}")
    print("Envio gratis")
