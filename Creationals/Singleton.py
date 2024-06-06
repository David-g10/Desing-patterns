
"""
********************************    Usando decoradores: *********************************
"""
def singleton(cls):

    instances = {}
  
    def get_instance(*args, **kwargs):

        if cls not in instances:
			
            instances[cls] = cls(*args, **kwargs)   
			
        return instances[cls]

    return get_instance


@singleton
class MySQLDatabase:

	def connect(self): 
		if self.connection is None: 
			# Lógica para establecer la conexión a la base de datos 
			self.connection = "Conexión establecida" 
			print("Conexión establecida") 
		else: 
			print("Ya estamos conectados") 
			
	def execute_query(self, query):
		if self.connection: 
			return f"Ejecutando consulta: {query}" 
		else: 
			return "No hay conexión a la base de datos"

  
@singleton
class PostgreSQLDatabase:

	def __init__(self, port):
		self.port = port

	def connect(self): 
		if self.connection is None: 
			# Lógica para establecer la conexión a la base de datos 
			self.connection = "Conexión establecida" 
			print("Conexión establecida") 
		else: 
			print("Ya estamos conectados") 
			
	def execute_query(self, query):
		if self.connection: 
			return f"Ejecutando consulta: {query}" 
		else: 
			return "No hay conexión a la base de datos"


# Ejemplo de uso
MySql_conn_1 = MySQLDatabase()
MySql_conn_2 = MySQLDatabase()

print(MySql_conn_1 == MySql_conn_2, "-> Es la misma conexion a DB porque los objetos provienen de un singleton")  # Resultado es True porque es una unica instancia.

# Otro Ejemplo de uso
PostgreSQL_conn_1 = PostgreSQLDatabase('442') # como podemos ver podemos pasar los parametros del constructor con normalidad, cosa que creando el singleton modificando el metodo __new__ de una clase no se puede lograr.


# ------------------------------------------------------------------------------------------------------------

"""
********************** Usando metaclases *********************************************
"""

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 42

# Uso
obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2, "-> Using metaclass")  # True


# --------------------------------------------------------------------------------------------------------------------

"""
***************** Usando una clase Base *****************************************
"""


class SingletonBase:
    _instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

class MyClass(SingletonBase):
    def __init__(self):
        self.value = 42

# Uso
obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2, "-> Using base class")  # True
