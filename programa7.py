'''hacer un programa que lea  nombre edad y sexo de 5 persona estos elementos deben estar en una lista'''

def Inicio():
    c =0 
    n = 0
    e = 0
    s = 0
    
    while True:
     n = input('Escribe un nombre')
     e = input('Escribe una edad')
     s = input('Escribe el sexo')
     lista.append(n + e + s)
     c += 1
     if c >=5:
         break
    print(lista)
 
    lista = []

if __name__ == '__main__': 
    Inicio() 