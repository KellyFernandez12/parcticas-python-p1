
def resultados():
    #  Función que muestra los resultados finales
    #  Function that shows the final results
    c2 = 0
    print(f'La lista tiene {len(car)} elementos')
    #  Muestra cuántos elementos hay en la lista "car"
    #  Print how many elements are in the list "car"

    for i in arr: 
        #  Recorremos cada posición del arreglo
        #  Loop through each position in the array
        if i != -1:
            #  Si el valor no es -1, significa que es un número válido
            #  If the value is not -1, it means it’s a valid number
            c2 += 1

    print(f'El arreglo tiene {c2} elementos')
    #  Muestra cuántos números válidos hay en el arreglo
    # Print how many valid numbers are in the array

    print("Lista:", car)
    # Imprime los elementos guardados en la lista
    # Print the elements stored in the list

    print("Arreglo:", arr)
    # Imprime el contenido del arreglo completo
    # Print the full content of the array


def hola():  # define método o función | define method or function
    c = 0
    while True:
        #  Ciclo infinito hasta que se ingresen 10 datos
        #  Infinite loop until 10 inputs are entered
        a = input('Escribe un dato o valor \n') 
        #  Pide al usuario un valor (número o texto)
        # Ask the user for a value (number or text)

        if a.isdigit():
            #  Si es un número, lo guarda en el arreglo en la posición c
            #  If it’s a number, store it in the array at position c
            arr[c] = int(a)
        elif a.isalpha():
            #  Si es texto, lo guarda en la lista
            #  If it’s text, store it in the list
            car.append(a)

        c += 1
        #  Aumenta el contador de datos ingresados
        #  Increase the counter of entered data

        if c >= 10:
            #  Si ya se ingresaron 10 datos, rompe el ciclo
            #  If 10 inputs have been entered, break the loop
            break


# Variables globales
arr = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]  
# Arreglo con 10 posiciones inicializadas en -1
# Array with 10 positions initialized to -1

car = []  
#  Lista vacía para guardar caracteres
#  Empty list to store characters


if __name__ == "__main__": 
    #  Punto de entrada del programa principal
    #  Main entry point of the program
    hola()         # Llama a la función para pedir los datos | EN: Call the function to request inputs
    resultados()   # Muestra los resultados al final | EN: Show results at the end
