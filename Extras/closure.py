
# Concepto importante por que es a partir de este que funcionan los decoradores!.


"""
Un Closure (cierre) es un objeto de función que recuerda los valores en los ámbitos incluídos, incluso si no están presentes en la memoria. Veámoslos paso a paso

Primero de todo, una Función Anidada es una función definida dentro de otra función. 
Es muy importante apuntar que las funciones anidadas pueden acceder a las variables 
de la función principal. Sin embargo, al menos en Python, son sólo de lectura, aunque
 se puede usar la palabra clave "nonlocal" explicitamente con esas variables para modificarlas.
"""

def add_new_numbers():  #Enclosing or main function.
    numbers = []
    def inner(num): # Inner or secundary function
        if num not in numbers:
            numbers.append(num)
        return numbers
    return inner


if __name__ == '__main__':
    p1 = add_new_numbers()
    print(p1(1))  # Llamamos a la función inner y vemos los cambios
    print(p1(2))  # Verificamos que el estado se mantiene entre llamadas
    print(p1(2))  # Verificamos que el estado se mantiene entre llamadas


    p2 = add_new_numbers() # Verificamos que el estado se mantiene para la nueva instancia
    print(p1(3))  
    print(p1(4))  
    print(p1(5))  
    print(p1(5))  

