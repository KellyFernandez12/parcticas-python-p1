'''Hacer un programa que en una lista se introduzca cadenas de caracteres con las siguientes restricciones:
1- Las cadenas no deben tener espacios
2- La cadena solo puede tener mayuscula la primer letra
3- Obligatoriamente tiene que tener todas las vocales (a,e,i,o,u)
El programa no termina hasta que la lista tenga 5 elementos'''

'''Make a program that stores character strings in a list with the following restrictions:
1- The strings must not contain spaces
2- The string can only have the first letter in uppercase
3- It must necessarily contain all vowels (a, e, i, o, u)
The program does not end until the list has 5 elements'''

def inicio():
    #Declara la función inicio()
    #Declares the function inicio()
    c = 0
    #Inicializa un contador c en 0
    #Initializes a counter c to 0
    vocales = set("aeiou")
    #Crea un set con las vocales mínimas para usar en la comprobación vocales
    #Creates a set with the vowels to use in the vowel check
    lista = []
    #Inicializa la lista global llamada lista
    #Initializes the global list named lista

    while True:
        #Empieza un bucle infinito; la salida se consigue con break.
        #Starts an infinite loop; the exit is achieved with break.

        cadena = input('Escribe una cadena: \n')
        #Pide al usuario que escriba una cadena y lo guarda en variable cadena
        #Asks the user to enter a string and stores it in variable cadena

        if " " in cadena:
            #Comprueba si hay un espacio en la cadena.
            #Checks if there is a space in the string.
            print('No debe contener espacios\n')
            #Si la cadena contiene espacios, muestra un mensaje de error.
            #If the string contains spaces, shows an error message.

        if not cadena[0].isupper():
            print('La primera letra debe ser mayuscula')
            #Comprueba si el primer carácter no es mayuscula e imprime mensaje
            #Checks if the first character is not uppercase and prints a message

        if not vocales.issubset(cadena.lower()):
            print('Debe contener todas las vocales')
            #Convierte la cadena a minúsculas y verifica si el conjunto vocales está incluido en los caracteres de la cadena
            #Converts the string to lowercase and checks if the set of vowels is included in the characters of the string

        
        c += 1
        #Incrementa el contador c siempre, aunque la entrada haya sido inválida.
        #Increments the counter c always, even if the entry was invalid.

        
        if c > 5:
            break
            #Comprueba si ya se han hecho 5 entradas si lo esta cierra con break
            #Checks if 5 entries have already been made; if so, closes with break

        lista.append(cadena)
        #Añade la cadena a la lista global lista
        #Adds the string to the global list called lista
        print(lista)
        #Imprime la lista
        #Prints the list

if __name__ == '__main__': #METODO PRINCIPAL / MAIN METHOD
    inicio()
    #Llama a la función inicio() para iniciar el programa
    #Calls the function inicio() to start the program