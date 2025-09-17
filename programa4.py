
'''
Hacer un programa que lea 10 numeros y los almacene en un arreglo
Make a program that reads 10 numbers and stores them in an array
'''

a = []   #Lista vacía para almacenar los números | Empty list to store the numbers
s = 0    #Variable para la suma total |  Variable for the total sum
n = 0    #Contador de cuántos números se han ingresado | Counter for how many numbers have been entered
numeros = "0123456789"  # Cadena con los dígitos válidos | String with valid digits

while (n < 10):  
    # Se repite hasta que se ingresen 10 números válidos  
    # Repeats until 10 valid numbers are entered  

    b = input('Escribe un numero: ')  
    # Pedimos un número como texto | Ask for a number as text  

    x = 0  
    for i in b:  
        #  Recorremos cada carácter del texto ingresado  
        # Loop through each character of the entered text  
        if i in numeros:  
            # Verificamos si el carácter es un dígito  
            # Check if the character is a digit  
            x += 1  

    if len(b) == x:  
        # Si todos los caracteres son dígitos, el número es válido  
        # If all characters are digits, the number is valid  
        a.append(int(b))  # Convertimos a entero y lo guardamos | Convert to integer and store it  
        n += 1  
    else:  
        print('El valor no es número')  
        # Mensaje de error si no es número |  Error message if it’s not a number  

# Recorremos la lista para imprimir los números y calcular la suma  
# Loop through the list to print the numbers and calculate the sum  
for i in a:  
    print(i)  
    s += i  

print(f'La suma es {s}')  
# Imprime la suma total de los números | EN: Print the total sum of the numbers 

