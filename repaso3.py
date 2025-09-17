
def validar(a):   # Define function validar with parameter a / Define función validar con parámetro a
    c = 0         # Initialize integer variable c / Inicializar variable entera c
    d = 0.0       # Initialize float variable d / Inicializar variable flotante d
    
    # First try: check if it's an integer
    # Primer intento: verificar si es un número entero
    try:
        c = int(a)   # Try to convert a to int / Intentar convertir a a entero
        print('Es un valor numérico entero (sin decimales)')  # If success, print message / Si tiene éxito, imprimir mensaje
        return        # Exit function after success / Salir de la función después del éxito
    except ValueError:  # If conversion fails / Si la conversión falla
        print('No es un número entero (sin decimales)')  # Print message / Imprimir mensaje

    # Second try: check if it's a float
    # Segundo intento: verificar si es un número decimal
    try:
        d = float(a)   # Try to convert a to float / Intentar convertir a a decimal (float)
        print('Es un valor numérico decimal (con o sin decimales)')  # Success message / Mensaje de éxito
    except ValueError:  # If conversion fails / Si la conversión falla
        print('No es un número decimal válido')  # Print message / Imprimir mensaje


def leer():   # Define function leer / Definir función leer
    # ord obtiene el código ASCII de un carácter
    # isalpha verifica si es letra
    # isdigit verifica si es número
    # try-except maneja errores de conversión
    
    a = input('Escribe un dato o valor: ')   # Ask user for input / Pedir al usuario un dato
    validar(a)   # Call validar with input / Llamar a validar con el dato ingresado


# Entry point of the program
# Punto de entrada del programa
if __name__ == '__main__':   # Check if file is executed directly / Verificar si el archivo se ejecuta directamente
    leer()   # Call leer() to start program / Llamar a leer() para iniciar el programa

   
