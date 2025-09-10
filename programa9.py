'''hacer un programa que en una lista se introdusca cadena de caracteres con las siquientes restricciones
    1 las cadenas no deben tener espacios 
    2 solo puede tener mayuscula la primera letra
    3 oblicatoria mente debe tener todas las vocales.
    el programa no termina hasta que la lista tenga 5 elementos'''

'''def vocales(cad):
 ba = False
 be = False
 bi = False
 bo = False
 bu = False
# for i in cad:
 if 'a' in cad or 'A' in cad:
    ba = True
 if 'e' in cad or 'E' in cad:
    be = True
 if 'i' in cad or 'I' in cad:
    bi = True
 if 'o' in cad or 'O' in cad:
    bo = True
 if 'u' in cad or 'U' in cad:
    bu = True   
 if ba == True and be == True and bi == True and bo == True and bu == True:
   
 

 def minusculas(c1):
  print(c1)
  for i in c1[1:]:
    if ord(i) >=97 and ord(i) <=122:
      cm += 1
      if cm == len(c1)-1:
        print(f'la cadena son minusculas execto la primera{cm}')
      else:
        print('Error la cadena no cumple')



  def leer():
   nc = " "
  co = 0
  c = input('Escribe una cadena')
  for i in c:
   if ord(i) !=32:
     co += 1
     
     if co == len(c):
       if c.isalpha():
         minusculas(c)

       else :
            for i in c:
             if ord(i)>=48 and ord(i) <=57:
               pass
             else:
               nc += 1
               print(nc)




lista = []
if __name__ == '__main__': 
    minusculas() 
    leer(
     if len(lista)>=5:
    )'''
