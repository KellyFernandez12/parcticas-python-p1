'''
Hacer un programa que lea 10 numeros y los almacene en arreglo
'''

a = [0,0,0,0,0,0,0,0,0,0]   
#Creamos una lista con 10 elementos inicializados en 0  
#Create a list with 10 elements initialized to 0 

for i in range(0,10):
#Creamos una lista con 10 elementos inicializados en 0  
#Create a list with 10 elements initialized to 0 

  a[i] = int (input(f'Escribe un numero {i}: '))  
  #Pedimos un número al usuario, lo convertimos a entero y lo guardamos en la posición i de la lista  
  #Ask the user for a number, convert it to integer, and store it at position i of the list  

for i in a:     #Recorremos cada valor almacenado en la lista "a"  | Loop through each value stored in list "a" 
    
    print(i)  #Imprimimos cada número ingresado por el usuario  | Print each number entered by the user  