
def validar(a):
    c = 0
    d = 0.0
    try:
     c = int(a)
     print('Es un valor numerico sin decimales')
    except ValueError:
     print('No es un valor numerico sin decimales') 
    try:
       d = float(a) 
       print('Es un valor numerico sin decimales')
    except ValueError:
     print('No es un valor numerico sin decimales') 

def leer(): 
# ord que obtiene el ascii del caracter
# isalpha para caracteres
# isdigit para numeros
# try except ValueError:

  a = input('Escribe un dato o valor')
  validar(a)


  if __name__ == '__main__':
    leer()

   
