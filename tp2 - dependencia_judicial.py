# Definición del tipo Dependencia Judicial.
# Estructura de representación: {fuero:string; nombre:string; direccion:string; localidad:string}
class DependenciaJudicial:
    
    # Función que se ejecuta al crear un nuevo elemento de tipo DependenciaJudicial:
    # dependencia representa cada una de las dependencias judiciales y v cada uno de los atributos:
    def __init__(self, linea):
        v = dependencia.split(";")
        self._numero = v[0]
        self._fuero = v[1]
        self._nombre = v[2]
        self._tipo_de_ente = v[3]
        self._direccion = v[4]
        self._localidad = v[5]
        self._departamento_judicial = v[6]
        self._telefono = v[7]
        self._latitud = float(v[8].replace(',','.'))
        self._longitud = float(v[9].replace(',','.'))
    
    # Devuelve el fuero de una dependencia judicial.
    def fuero(self):
        return self._fuero
    
    # Devuelve el nombre de una dependencia judicial.
    def nombre(self):
        return self._nombre
    
    # Devuelve el tipo de ente de una dependencia judicial.
    def tipo_de_ente(self):
        return self._tipo_de_ente
    
    # Devuelve la dirección de una dependencia judicial.
    def direccion(self):
        return self._direccion
    
    # Devuelve la localidad de una dependencia judicial.
    def localidad(self):
        return self._localidad
    
    # Devuelve el departamento judicial de una dependencia judicial.
    def departamento_judicial(self):
        return self._departamento_judicial
    
    # Devuelve el teléfono de una dependencia judicial.
    def telefono(self):
        return self._telefono
    
    # Devuelve la latitud de una dependencia judicial.
    def latitud(self):
        return self._latitud
    
    # Devuelve la longitud de una dependencia judicial.
    def longitud(self):
        return self._longitud
    
    # Devuelve la distancia euclídea (float) entre la dependencia judicial dj y el punto(lat,lng).
    def distancia(self, lat, lng):
        distancia = (((float(self._latitud) - float(lat))**2) + ((float(self._longitud) - float(lng))**2))**0.5
        return float(distancia)
    
    def __hash__(self):
        return hash((self._fuero, self._nombre, self._tipo_de_ente, self._direccion, self._localidad, self._departamento_judicial, self._latitud, self._longitud))
    
    # Devuelve una expresion booleana si son iguales las dependencias judiciales que se pasan como argumentos.
    def __eq__ (self, other):
        return self._fuero == other._fuero and self._nombre == other._nombre and self._departamento_judicial == other._departamento_judicial
    
    # Devuelve una expresion booleana si la dependencia judicial (self) es menor estricto que la dependencia judicial (other).
    def __lt__(self, other):
        return self._departamento_judicial < other._departamento_judicial or \
               self._departamento_judicial == other._departamento_judicial and self._fuero < other._fuero or \
               self._departamento_judicial == other._departamento_judicial and self._fuero == other._fuero and self._nombre < other._nombre    
    
    # Devuelve el string que se muestra cuando se imprime una dependencia judicial.
    def __repr__(self):
        return "{" + self._fuero + ";" + self._nombre + ";" + self._direccion + ";" + self._localidad + "}"
