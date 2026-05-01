from excepciones import ClienteError 

#Creamos la clase cliente
class Cliente:

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

#Encapsulacion nombre
@property
def nombre(self):
        return self.__nombre

@nombre.setter
def nombre(self, valor):
        if not valor or len(valor.strip()) < 5:
            raise ClienteError("El nombre debe tener mínimo 5 caracteres")
        self.__nombre = valor
#Encapsulacion correo
@property
def correo(self):
        return self.__correo

@correo.setter
def correo(self, valor):
        if not valor or"@" not in valor or "." not in valor:
            raise ClienteError("Correo electrónico inválido")
        self.__correo = valor

def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo}"

        