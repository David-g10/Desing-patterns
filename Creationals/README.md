# SINGLETON

El patrón Singleton es un patrón de diseño creacional que garantiza que una clase tenga solo una instancia y proporciona un punto de acceso global a esta instancia. Esto significa que no importa cuántas veces se solicite la creación de un objeto de esa clase, siempre se devuelve la misma instancia.

**Características:**

- **Única instancia:** Garantiza que solo haya una instancia de la clase en todo el programa.
- **Acceso global:** Proporciona un punto de acceso global a la instancia única de la clase.
- **Inicialización diferida:** La instancia única se crea solo cuando es solicitada por primera vez, lo que mejora la eficiencia al evitar la creación anticipada de objetos.
- **Control sobre la creación de instancias:** El patrón Singleton controla la creación y acceso a la única instancia de la clase, evitando que los clientes creen instancias adicionales.
- **Gestión de recursos compartidos:** Útil cuando necesitas gestionar recursos compartidos, como conexiones a la base de datos o archivos, de manera que se evite la duplicación de recursos y se mantenga la consistencia en su uso.


## Extras:
Una de las aplicacion mas cotidianas del patron singleton es para gestionar la conexion a base de datos en una app.

1. **Uso concurrente de la conexión a la base de datos**: El patrón Singleton no afecta la disponibilidad de la conexión a la base de datos para varias solicitudes concurrentes. Cuando múltiples partes de la aplicación necesitan acceder a la base de datos al mismo tiempo, la única instancia Singleton manejará estas solicitudes concurrentes de manera transparente. La conexión a la base de datos generalmente está diseñada para ser utilizada por múltiples clientes simultáneamente, por lo que el Singleton no tiene que esperar a que una solicitud termine antes de atender a otra. Cada solicitud que requiera acceso a la base de datos simplemente utiliza la misma instancia Singleton para realizar la operación necesaria. Sin embargo, es importante asegurarse de que la implementación de la conexión a la base de datos sea segura y que maneje adecuadamente la concurrencia para evitar problemas como condiciones de carrera o bloqueos.
    
2. **Cierre de la conexión**: En muchos casos, el Singleton no cierra la conexión a la base de datos. La idea es mantener la conexión abierta para evitar el costo asociado con la apertura y cierre repetidos de la conexión. Sin embargo, dependiendo de la implementación y los requisitos específicos de la aplicación, puede ser necesario implementar lógica adicional para administrar el ciclo de vida de la conexión, como cerrar la conexión después de un período de inactividad o cuando la aplicación se apaga.
    
3. **Costo de mantener la conexión abierta**: Mantener la conexión abierta puede consumir recursos, como memoria y recursos del servidor de base de datos. Es importante encontrar un equilibrio entre el rendimiento y la eficiencia de recursos. En aplicaciones de alta concurrencia o en entornos donde los recursos son limitados, puede ser necesario implementar mecanismos para administrar la cantidad de conexiones abiertas, como establecer límites en el número máximo de conexiones o implementar la liberación de conexiones inactivas después de un tiempo determinado. Esto puede ayudar a mitigar el impacto en los recursos del sistema y garantizar un funcionamiento óptimo de la aplicación.


# **BUILDER**

Se puede identificar la necesidad de usar el patrón Builder en las siguientes situaciones:

1. **Objetos Complejos con Múltiples Configuraciones**: Cuando necesitas construir objetos complejos que requieren múltiples configuraciones o pasos.
    
2. **Reutilización y Flexibilidad**: Cuando necesitas crear múltiples variaciones del mismo objeto y deseas evitar la duplicación de código.
    
3. **Mejora de la Claridad del Código**: Cuando el proceso de construcción de objetos se vuelve complicado y deseas mejorar la claridad y mantenibilidad del código.
    
4. **Separación de Concerns**: Cuando quieres separar la lógica de construcción de la lógica del negocio, manteniendo el código más modular y fácil de mantener.
    
5. **Exceso de clases hijos:**: Cuando ves que se empiezan a crear y crear clases de un padre buscando que cada una tenga sus nuevas propias caracteriscas diferenciales.

En resumen, el patrón Builder es útil en situaciones reales donde se necesita construir objetos complejos de manera flexible y modular, mejorando la claridad, mantenibilidad y reutilización del código.

Combinar el patrón Builder con `Enum` en Python puede traer beneficios adicionales, especialmente en términos de claridad y seguridad del código. Veamos qué es `Enum`, cómo se usa y qué beneficios trae cuando se combina con el patrón Builder.

### Qué es `Enum` en Python

`Enum` (abreviatura de "enumeration") es una clase en Python que permite definir un conjunto de valores simbólicos constantes. Cada miembro de una `Enum` es una constante con un nombre y un valor únicos. Se utiliza para representar un grupo de valores relacionados de manera clara y segura.

#### Beneficios de Usar `Enum`

1. **Claridad y Legibilidad**: Al usar `Enum`, puedes dar nombres descriptivos a un conjunto de valores relacionados, lo que mejora la claridad y legibilidad del código.
    
2. **Seguridad en el Tipo**: `Enum` ayuda a prevenir errores al garantizar que solo se usen valores válidos. Esto es especialmente útil cuando tienes un conjunto fijo de opciones y quieres evitar valores no válidos.
    
3. **Mantenimiento Simplificado**: Los valores de `Enum` son fáciles de mantener y actualizar. Si necesitas agregar o cambiar un valor, puedes hacerlo en un solo lugar.