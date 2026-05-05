from excepciones import ReservaError
from logger import registrar_log

class Reserva:

    def __init__(self, cliente, servicio, duracion):
        try:
            if cliente is None:
                raise ReservaError("El cliente no puede ser nulo")

            if servicio is None:
                raise ReservaError("El servicio no puede ser nulo")

            if duracion <= 0:
                raise ReservaError("La duración debe ser mayor a 0")

            self._cliente = cliente
            self._servicio = servicio
            self._duracion = duracion
            self._estado = "pendiente"
            self._costo = 0

        except Exception as e:
            registrar_log(f"Error al crear la reserva: {e}")
            raise

    def confirmar(self):
        try:
            if self._estado == "confirmada":
                raise ReservaError("La reserva ya está confirmada")

            if self._estado == "cancelada":
                raise ReservaError("No se puede confirmar una reserva cancelada")

            self._estado = "confirmada"

        except Exception as e:
            registrar_log(f"Error al confirmar: {e}")
            raise

    def cancelar(self):
        try:
            if self._estado == "cancelada":
                raise ReservaError("La reserva ya está cancelada")

            if self._estado == "confirmada":
                raise ReservaError("No se puede cancelar una reserva ya confirmada")

            self._estado = "cancelada"

        except Exception as e:
            registrar_log(f"Error al cancelar: {e}")
            raise

    def procesar(self, descuento=0):
        try:
            if self._estado == "cancelada":
                raise ReservaError("No se puede procesar una reserva cancelada")

            self._costo = self._servicio.calcular_costo(self._duracion, descuento)

        except Exception as e:
            registrar_log(f"Error al procesar: {e}")
            raise
        else:
            self._estado = "confirmada"
            print("Reserva procesada correctamente")
        finally:
            print("Proceso finalizado")

    def mostrar(self):
        print(self._cliente.mostrar_info())
        print(f"Servicio: {self._servicio.descripcion()}")
        print(f"Duración: {self._duracion}")
        print(f"Estado: {self._estado}")
        print(f"Costo: {self._costo}")
