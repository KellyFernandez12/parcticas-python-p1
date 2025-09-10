
'''
Hacer un programa que lea 10 numeros y los almacene en arreglo
'''

a = []
s = 0
n = 0
numeros = "0123456789"
while (n < 10):
    b= input('Escribe un  numero')
    x= 0
    for i in b:
    # if (ord(i) >=48 and ord(i) <= 57):
     if i in numeros:
      x += 1
if len(b) == x:
      
      a.append(int(b))
      n += 1

else:
   print('el valor no es seguro')
   

for i in a:
 print (i)
 s += i
 print(f'La suma es {s}')

