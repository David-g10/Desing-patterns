from abc import ABC, abstractmethod

# Interfaz Componente:
class Bebida(ABC):
    @abstractmethod
    def costo(self):
        pass
    
    @abstractmethod
    def descripcion(self):
        pass

#------------------------------------------------------
# Componente Concreto:
class Cafe(Bebida):
    def costo(self):
        return 5.0
    
    def descripcion(self):
        return "Café"
    
#------------------------------------------------------
# Decorador:
class Aderezo(Bebida):
    def __init__(self, bebida):
        self._bebida = bebida
    
    def costo(self):
        return self._bebida.costo()
    
    def descripcion(self):
        return self._bebida.descripcion()
#------------------------------------------------------
# Decorador Concreto:
class Leche(Aderezo):
    def costo(self):
        return self._bebida.costo() + 1.5
    
    def descripcion(self):
        return self._bebida.descripcion() + ", Leche"

class Azucar(Aderezo):
    def costo(self):
        return self._bebida.costo() + 0.5
    
    def descripcion(self):
        return self._bebida.descripcion() + ", Azúcar"
#------------------------------------------------------
# Uso del Patrón:
if __name__ == '__main__':
    # Café simple
    cafe = Cafe()
    print(cafe.descripcion())  # Output: "Café"
    print(cafe.costo())        # Output: 5.0

    # Café con leche
    cafe_con_leche = Leche(cafe)
    print(cafe_con_leche.descripcion())  # Output: "Café, Leche"
    print(cafe_con_leche.costo())        # Output: 6.5

    # Café con leche y azúcar
    cafe_con_leche_y_azucar = Azucar(cafe_con_leche)
    print(cafe_con_leche_y_azucar.descripcion())  # Output: "Café, Leche, Azúcar"
    print(cafe_con_leche_y_azucar.costo())        # Output: 7.0
