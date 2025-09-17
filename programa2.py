

#Areglo | Array
a= [10] # arreglo con un solo elemento inicializado en 10  |  array with a single element initialized with 10


a[0] = 10    # asignamos el valor 10 en la posición 0   |  assign value 10 at position 0 

a[1] = 10  # asignamos el valor 10 en la posición 1   |  assign value 10 at position 1 

#Lista | List
b = [] # lista vacía (sin elementos)  |  empty list (no elements)

b = {'hola',10,10.05,False,'m',{1,2,3,4}}   # conjunto con diferentes tipos de datos (string, int, float, bool, string, y otro set)  
# set with different data types (string, int, float, bool, string, and another set)


#ciclos y condiciones |  loops and conditions
if(len(a) > len(b)):
    # si la longitud de a es mayor que la longitud de b  |  if the length of a is greater than the length of b 
    print('A es mayor') # imprime que A es mayor  |  prints that A is greater
else:
    print('B es mayor') # imprime que B es mayor  |  prints that B is greater

for i in a:
    # recorre cada elemento en a  |  loop through each element in a
    print(i) # imprime el valor de i  |  prints the value of i