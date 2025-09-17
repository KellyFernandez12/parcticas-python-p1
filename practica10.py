
def vocales(cad):
    # Declara la función vocales que recibe un parámetro cad
    # Declares the function vocales that receives a parameter cad
    ba = False
    bc = False
    bi = False
    bo = False
    bu = False
    # Inicializa las variables booleanas en False
    # Initializes the boolean variables as False

    if 'a' in cad or 'A' in cad:
        ba = True
    if 'e' in cad or 'E' in cad:   # ← corregido aquí
        bc = True
    if 'i' in cad or 'I' in cad:
        bi = True
    if 'o' in cad or 'O' in cad:
        bo = True
    if 'u' in cad or 'U' in cad:
        bu = True
    # Si la vocal está en la cadena cad, se marca la variable correspondiente como True
    # If the vowel is in the string cad, the corresponding variable is marked as True

    if ba == True and bc == True and bi == True and bo == True and bu == True:
        # Comprueba si todas las vocales están presentes
        # Checks if all vowels are present
        lista.append(cad)
        # Si la condición es verdadera, agrega la cadena cad a la lista
        # If the condition is true, add the string cad to the list
    print(lista) 
    # Imprime la lista "lista"
    # Prints the list "lista"

def minusculas(cl):
    # Declara la función minusculas que recibe cl
    # Declares the function minusculas that receives cl
    cm = 0
    # Contador de caracteres en minúscula (excepto el primero)
    # Counter for lowercase characters (except the first)
    print(cl)
    # Imprime la cadena recibida
    # Prints the received string

    for i in cl[1:]:
        # Recorre la cadena desde el segundo carácter
        # Iterates the string starting from the second character
        if ord(i) >=97 and ord(i) <=122:
            # Comprueba si el carácter es minúscula con ASCII
            # Checks if the character is lowercase using ASCII
            cm += 1
            # Incrementa el contador
            # Increments the counter

    if cm == len(cl)-1:
        # Si todos los caracteres (menos el primero) son minúsculas
        # If all characters (except the first) are lowercase
        print(f'la cadena son minusculas excepto la primera({cm})')
        vocales(cl)
        # Llama a la función vocales pasándole cl
        # Calls the function vocales passing cl
    else:
        print('Error en la cadena')
        # Muestra un error si no cumple con la condición
        # Shows an error if condition is not met

def leer():
    # Declara la función leer
    # Declares the function leer
    con = 0 
    # Contador de caracteres distintos de espacio
    # Counter of characters different from space
    nc = "" 
    # Nueva cadena vacía
    # New empty string
    c = input('Escribe una cadena \n')
    # Pide al usuario ingresar una cadena
    # Prompts user to enter a string

    for i in c:
        if ord(i) != 32:
            con += 1
    # Comprueba que no sean espacios, si no lo son, incrementa con
    # Checks that characters are not spaces, if not, increments con

    if con == len(c):
        # Si la longitud coincide, no hay espacios
        # If the length matches, there are no spaces
        if c.isalpha():
            # Si son solo letras
            # If only letters
            minusculas(c)
        else:
            for i in c:
                if ord(i)>=48 and ord(i)<=57:
                    pass
                    # Si es un número no hace nada
                    # If it is a number, does nothing
                else:
                    nc += i
                    # Copia el carácter que no es número
                    # Copies the character that is not a number
            print(nc) 
            # Imprime la nueva cadena sin números
            # Prints the new string without numbers
            minusculas(nc)
            # Llama a minusculas con la cadena filtrada
            # Calls minusculas with the filtered string
    else:
        print('Error en la cadena')
        # Si contiene espacios, muestra error
        # If it contains spaces, shows error

lista = [] 
# Crea la lista global
# Creates the global list

if __name__== '__main__': 
    # Punto de entrada del programa
    # Program entry point
    while(True): 
        # Bucle infinito
        # Infinite loop
        leer()
        # Llama a la función leer
        # Calls the function leer
        if len(lista) >=5:
            # Detiene el ciclo cuando lista tenga 5 elementos
            # Stops the loop when list has 5 elements
            break