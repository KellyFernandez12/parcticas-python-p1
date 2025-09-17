'''
hacer un programa que lea 10 dato, si el dato es un numero se almacenara en un arreglo si es un carcter o caracteres se metera
a una lista, cuando finalice el programa nos mostrara cuanto elementos unmerico y cuantos caracteres hay el cada estructura
'''

arr=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]  
# Arreglo con 10 posiciones inicializadas en -1 (espacios vacíos)  
#  Array with 10 positions initialized to -1 (empty slots)  

car = []   
# Lista vacía para guardar caracteres o cadenas  
# Empty list to store characters or strings  

c = 0      
#  Contador general de datos ingresados  
# General counter of entered data  

c2 = 0     
#  Contador para los números válidos almacenados  
#  Counter for valid numbers stored  

while(True):  
    # Ciclo infinito que se rompe manualmente después de 10 datos  
    # Infinite loop that breaks manually after 10 inputs  

    a = input('Escribe un dato o valor: ')   
    # Pide un dato al usuario (puede ser número o texto)  
    # Ask the user for input (can be number or text)  

    if a.isdigit():  
        # Si el dato es un número (solo dígitos)  
        # If the input is a number (digits only)  

        arr[c] = int(a)     
        # Convierte el dato a entero y lo guarda en el arreglo en la posición c  
        # Convert the input to integer and store it in the array at position c  

    elif a.isalpha():  
        # Si el dato son solo letras (caracteres o cadenas)  
        # If the input is only letters (characters or strings)  

        car.append(a)       
        # Agrega el valor a la lista de caracteres  
        # Append the value to the character list  

    c += 1   
    # Incrementa el contador de datos ingresados  
    # Increase the counter of entered data  

    if c >= 10:            
        #  Si ya se ingresaron 10 datos, salir del ciclo  
        #  If 10 inputs have been entered, exit the loop  

        break  
        # Rompe el ciclo while  
        # Break the while loop  


print(f'La lista tiene {len(car)} elementos')  
#  Imprime cuántos elementos se guardaron en la lista  
#  Print how many elements were stored in the list  

for i in arr:  
    #  Recorre cada posición del arreglo  
    #  Loop through each position in the array  

    if i != -1:            
        #  Cuenta solo los valores que no son -1 (espacios llenos)  
        #  Count only values different from -1 (filled slots)  

        c2 += 1  
        # Incrementa el contador de números válidos  
        # Increase the counter of valid numbers  

print(f'El arreglo tiene {c2} elementos')  
# Imprime cuántos números se almacenaron en el arreglo  
# Print how many numbers were stored in the array  

print("Lista:", car)  
# Muestra el contenido de la lista de caracteres  
# Show the content of the character list  

print("Arreglo:", arr)  
# Muestra el contenido del arreglo con números y -1 en posiciones vacías  
# Show the content of the array with numbers and -1 in empty positions  