'''
hacer un programa que lea 10 dato, si el dato es un numero se almacenara en un arreglo si es un carcter o caracteres se metera
a una lista, cuando finalice el programa nos mostrara cuanto elementos unmerico y cuantos caracteres hay el cada estructura
'''
'''
l = []
a = [0,0,0,0,0,0,0,0,0,0]
numeros = "0123456789"
nombres = " "

for i in range(0,10):
  a[i] = int (input('Escribe un numero /n'))  
for i in a:
    print(i) 
'''
#codigo del profe

arr=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
car = []
c = 0
c2 = 0
while(True):
   a= input('Escribe un dato o valor \n') 
   if a.isdigit():
      arr [c - 1] = int(a)
   elif a.isalpha():
    car.append(a)
   c += 1 
   if c >10:
      break
      print(f'el arreglo tiene {len(car)}')
      for i in arr:
       if i != 0:
        c2 += 1
        print(f'el arreglo tiene {c2}')
        print(car)
        print(car)

