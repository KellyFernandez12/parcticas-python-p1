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

'''Hacer un programa que lea nombre y precio de un producto el programa calculara 
el costo y precio de venta
el costo involucra el 12$ y iva 16%'''


for i in range(1,5):
   nombre = input('Escribe el producto')
   precio = float(input('Escribe el precio'))
   precio = 15
   costo = precio * .12
   precioventa = costo * .16
   print(f'el costo{costo: .2f} y el precio venta{precioventa : .2f}')
   print(f'el costo{costo} y el precio venta{precioventa}')
   res = input('Deseas otro numero (s/n) \n')
   if res == 'n' or res == 'N':
     break
     
  





