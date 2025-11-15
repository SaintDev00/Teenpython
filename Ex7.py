enú=12000

bebida=input("Quieres incluir bebida? yes/no" ).lower()

match bebida:
    case'yes':
        subtotal=Menú+3000
        precio_iva=subtotal*1.08
        print(f"Tu precio con iva es {precio_iva:.2f}")
    
    case 'no':
       subtotal=Menú
       precio_iva=subtotal*1.08
       print(f"Tu precio con iva es {precio_iva:.2f}")
       
