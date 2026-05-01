from abc import ABC, abstractmethod
from excepciones import ServicioError

class Servicio(ABC):

    def __init__(self, nonbre, tarifa_base):
        if not nonbre:
            raise ServicioError("el nombre del servicio no puede estar vacio")
        if tarifa_base  <= 0:
            raise ServicioError("La tarfa debe ser mayar que 0")
        
    self.nombre = nombre
    self.tarifa_base = tarifa_base

@abstractmethod
def calcular_costo(self, duracion, descuento=0)
    pass

@abstractmethod
def descripcion(self):
    pass
