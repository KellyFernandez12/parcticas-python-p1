'''
'''
#intrucciones de entrada y salida
#print() o print(f)
#print('Hola mundo')
#print(f'Hola mundo {10}')
#Entrada de datos
#input('Escribe un numero') #se introducen solo letras
#casting para convertir a valores especificos
#f  = float(input('Escribe un nuemro con decimales'))
#a = 0
#a = int(input('Escribe un numero'))
#c = 120
#print(str(c))
#v = ""
#v = str(c)
#Nota:solo las variables que no se introducen por teclado se obliga a inicializarlas

'''Hacer un programa que lea nombre y precio de un producto. 
El programa calculará el costo y precio de venta.
El costo involucra un 12% y el IVA 16%.'''

for i in range(1, 5):
    nombre = input('Escribe el producto: ')  
    # Pide el nombre del producto / Asks for product name
    
    precio = float(input('Escribe el precio: '))  
    # Pide el precio como número decimal / Asks for price as float

    costo = precio + (precio * 0.12)  
    # Costo = precio + 12% / Cost = price + 12%

    precioventa = costo + (costo * 0.16)  
    # Precio de venta = costo + 16% IVA / Sale price = cost + 16% VAT

    print(f'El producto "{nombre}" tiene un costo de {costo:.2f} y un precio de venta de {precioventa:.2f}')
    # Muestra el resultado con 2 decimales / Shows result with 2 decimals

    res = input('¿Deseas ingresar otro producto? (s/n): \n')  
    # Pregunta si se quiere repetir / Asks if user wants to continue

    if res.lower() == 'n':
        break
  





