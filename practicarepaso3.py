 #hacer un programa que lea un dato cual sea y que lo almacene en una lista respetando su tipo de dato

def validar(a):
    ne=0
    try:
       ne = int(a)
       return ne
    except ValueError:
       print('No es un entero')
       try:
          nf = float(a) 
          return nf
       except ValueError:
           print('No es un numero decimal')
           return a

def leer():
  a = input('Escribe un dato \n')
  dato = validar(a)
  lista.append(dato)  


lista = []

if __name__ == '__main__':
    while(True):
       leer()
       res = input ==('Deseas otros s/n')
       if res == 'n' or res == 'N':
          print(lista)
          break
