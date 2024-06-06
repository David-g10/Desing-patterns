from enum import Enum

class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    
print(HttpMethod.GET, "AJUUAAAAA")
## VENTAJAS DEL ENUM SOBRE ATRIBUTOS DE CLASE.
# Comparación segura
print(HttpMethod.GET == HttpMethod.GET)  # True
print(HttpMethod.GET == "GET")  # False
print(HttpMethod.GET.value == "GET")  # True

# Iteración sobre los miembros del Enum
for method in HttpMethod:
    print(method)

# vs atributos de clase
class HttpMethodClase():
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
print(HttpMethodClase.GET == "GET")  # True (pero menos claro y seguro)

# No se puede iterar directamente sobre los atributos
# Se necesita una implementación adicional


"""
                    IMPLEMENTACION DEL BUILDER
"""


class HttpRequest:
    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        self.params = {}
        self.body = None

    def __str__(self):
        return f"Method: {self.method}, URL: {self.url}, Headers: {self.headers}, Params: {self.params}, Body: {self.body}"

class HttpRequestBuilder():
    def __init__(self):
        self.request = HttpRequest()

    def set_method(self, method: HttpMethod):
        self.request.method = method.value
        return self

    def set_url(self, url):
        self.request.url = url
        return self

    def add_header(self, key, value):
        self.request.headers[key] = value
        return self

    def add_param(self, key, value):
        self.request.params[key] = value
        return self

    def set_body(self, body):
        self.request.body = body
        return self

    def build(self):
        return self.request


if __name__ == '__main__':
    # Uso del Builder con Enum para construir una solicitud HTTP
    builder = HttpRequestBuilder()
    request = (builder.set_method(HttpMethod.POST)
                    .set_url("https://api.example.com/data")
                    .add_header("Authorization", "Bearer token")
                    .add_param("query", "example")
                    .set_body({"key": "value"})
                    .build())
    print(request)
