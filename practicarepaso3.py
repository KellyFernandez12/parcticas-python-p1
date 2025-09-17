# Programa que lee un dato, detecta su tipo y lo guarda en una lista
# Program that reads a value, detects its type, and stores it in a list

def validar(a):   # Define function validar / Definir función validar
    ne = 0        # Variable for integer / Variable para enteros
    try:
        ne = int(a)   # Try to convert to int / Intentar convertir a entero
        return ne     # If success, return integer / Si tiene éxito, devolver entero
    except ValueError:
        print('No es un entero')   # Not an integer / No es un entero
        try:
            nf = float(a)          # Try to convert to float / Intentar convertir a decimal
            return nf              # Return float / Devolver decimal
        except ValueError:
            print('No es un número decimal')  # Not a float / No es un decimal
            return a               # Return as string / Devolver como texto


def leer():   # Define leer / Definir leer
    a = input('Escribe un dato: \n')   # Ask user input / Pedir dato al usuario
    dato = validar(a)                  # Validate type / Validar tipo de dato
    lista.append(dato)                 # Add to list / Agregar a la lista


lista = []   # Empty list / Lista vacía

# Entry point
# Punto de entrada
if __name__ == '__main__':
    while True:   # Infinite loop until user exits / Bucle infinito hasta que el usuario decida salir
        leer()    # Read and validate / Leer y validar
        res = input('¿Deseas ingresar otro dato? (s/n): ')   # Ask if continue / Preguntar si desea continuar
        if res == 'n' or res == 'N':   # If no / Si responde no
            print('Lista final:', lista)   # Show final list / Mostrar lista final
            break   # Exit loop / Salir del bucle