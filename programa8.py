''''Hacer un programa que lea una cadena y que muestre en pantalla 
cuantos numeros tiene, cuantas mayusculas, cuantas minusculas y cuantos espacios'''
''''Make a program that reads a string and shows on screen 
how many numbers, uppercase letters, lowercase letters, and spaces it has'''


def inicio():
    c = 0          # Contador de números | Number counter
    e = 0          # Contador de espacios | Space counter
    min = 0        # Contador de minúsculas | Lowercase counter
    may = 0        # Contador de mayúsculas | Uppercase counter
    numeros = "0123456789"   # Todos los dígitos válidos | All valid digits
    
    cadena = input('Escribe una cadena: \n')  # Pide la cadena al usuario | Asks user for input string
    
    for i in cadena:            # Recorre cada carácter de la cadena | Loops through each character
        if i in numeros:        # Si el carácter es un número | If the character is a digit
            print('Es numero')  # Imprime "Es numero" | Prints "Es numero"
            c += 1              # Suma al contador de números | Increments number counter
        
        if ord(i) == 32:        # Si el ASCII es 32 (espacio) | If ASCII is 32 (space)
            e += 1              # Suma un espacio | Adds one space
        
        if ord(i) >= 97 and ord(i) <= 122:   # Si está entre 'a' y 'z' | If it’s between 'a' and 'z'
            min += 1            # Cuenta minúscula | Counts lowercase
        
        if ord(i) >= 65 and ord(i) <= 90:    # Si está entre 'A' y 'Z' | If it’s between 'A' and 'Z'
            may += 1            # Cuenta mayúscula | Counts uppercase
    
    # Muestra los resultados finales | Displays final results
    print(f'\nLos numeros son: {c}\nLos espacios son: {e}\nLas minusculas son: {min}\nLas mayusculas son: {may}\n')


if __name__ == '__main__': 
    inicio()