'''Hacer un programa que lea una cadena y que muestre en pantalla 
cuantos nuemros tiene,cuantas mayusculas, cuantas minusculas y cuantos espacios'''
def inicio():
    c = 0
    e = 0
    min = 0
    may = 0
    numeros = "0123456789"
    cadena = input('Escribe una cadena')
    for i in cadena:
        if i in numeros:
            print('es numero')
            c += 1
            if ord(i)== 32:
                e += 1
            if ord(i)>=97 and ord(i)<=122:
                min += 1
            if ord(i)>=65 and ord(i)<=90:
                may += 1
    print(f'Los numeros son: {c}\n y los espacios son:{e}\n y las minusculas son: {min}\n y mayusculas son: {may}\n')            




if __name__ == '__main__': 
    inicio() 
    