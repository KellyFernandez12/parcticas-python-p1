

#
a = 0 
b = 0
c = 0
p = 0
m = 0
r = 0
ra = 0.0
d = 0.0
x1 = 0.0 
x2 = 0.0

p = b**2
m = 4*a*c
r = p - m
if r > 0:
    print('si se pudo')
    ra = r**(1/2)
    d = 2*a
    x1 = (-b + ra ) /d
    x2 = (-b - ra) /d
    print(f'El valor de x1 es {x1:.2f} y de x2(x2:.2f)')
else:
    print('No se puede')








