from abc import ABC, abstractmethod
from excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):
        if not nombre:
            raise ServicioError("El nombre del servicio no puede estar vacío")

        if tarifa_base <= 0:
            raise ServicioError("La tarifa debe ser mayor que 0")

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass
