'''hacer un programa que lea  nombre edad y sexo de 5 persona estos elementos deben estar en una lista'''
'''make a program that reads name, age, and gender of 5 people; these elements must be stored in a list'''

def Inicio(): # Define la función llamada Inicio / Defines the function called Inicio
    c =0  # Inicializa un contador en 0 / Initializes a counter at 0 

    lista = []   # Crea una lista vacía para guardar los datos / Creates an empty list to store the data
    
    while True: # Inicia un bucle infinito que se detendrá con break / Starts an infinite loop that will stop with break
     
     n = input('Escribe un nombre')  # Pide al usuario que escriba un nombre / Asks the user to input a name
     e = input('Escribe una edad') # Pide al usuario que escriba una edad / Asks the user to input an age
     s = input('Escribe el sexo')  # Pide al usuario que escriba el sexo / Asks the user to input a gender

     lista.append(n + e + s)  # Une nombre, edad y sexo en una sola cadena y la agrega a la lista  
       # Concatenates name, age, and gender into one string and adds it to the list
       
     c += 1    # Incrementa el contador en 1 / Increments the counter by 1
     if c >=5:   # Revisa si ya se ingresaron 5 personas / Checks if 5 people have been entered
         break # Si ya son 5, sale del bucle / If yes, breaks the loop
    print(lista) # Muestra la lista completa en pantalla / Prints the complete list

if __name__ == '__main__':  # Punto de entrada principal del programa / Main entry point of the program
    Inicio() # Llama a la función Inicio / Calls the Inicio function