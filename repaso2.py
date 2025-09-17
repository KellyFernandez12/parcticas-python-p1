

#
a = 1 
b = 2
c = 15

p = 0
m = 0
r = 0
ra = 0.0
d = 0.0
x1 = 0.0 
x2 = 0.0

# Calculate discriminant part values
# Calcular los valores parciales para el discriminante
p = b**2        # b squared / b al cuadrado
m = 4*a*c       # 4ac term / término 4ac
r = p - m       # discriminant (b² - 4ac) / discriminante (b² - 4ac)

# Check if discriminant is positive
# Verificar si el discriminante es positivo
if r > 0:
    print('si se pudo')  # Means solution is possible / Significa que hay solución
    
    # Square root of discriminant
    # Raíz cuadrada del discriminante
    ra = r**(1/2)  
    
    # Denominator of quadratic formula (2a)
    # Denominador de la fórmula cuadrática (2a)
    d = 2*a  
    
    # First solution
    # Primera solución
    x1 = (-b + ra ) / d  
    
    # Second solution
    # Segunda solución
    x2 = (-b - ra) / d  
    
    # Print results with formatting 
    # Imprimir resultados con formato
    print(f'El valor de x1 es {x1:.2f} y de x2{x2:.2f}')
else:
    # If discriminant is negative or zero, no real solution
    # Si el discriminante es negativo o cero, no hay solución real
    print('No se puede')








