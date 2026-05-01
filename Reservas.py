class Reserva:
    def __init__(self, cliente, servicio, duracion):
        try:
            if cliente is None:
                raise Exception("El cliente no puede ser nulo")

            if servicio is None:
                raise Exception("El servicio no puede ser nulo")

            if duracion <= 0:
                raise Exception("La duración debe ser mayor a 0")

            self._cliente = cliente
            self._servicio = servicio
            self._duracion = duracion

            self._estado = "pendiente"

            self._costo = 0

        except Exception as e:
            self._registrar_log(f"Error al crear la reserva: {e}")
            raise

    def confirmar(self):
        try:
            if self._estado == "confirmada":
                raise Exception("La reserva ya está confirmada")

            if self._estado == "cancelada":
                raise Exception("No se puede confirmar una reserva cancelada")

            self._estado = "confirmada"

        except Exception as e:
            self._registrar_log(f"Error al confirmar: {e}")

    def cancelar(self):
        try:
            if self._estado == "cancelada":
                raise Exception("La reserva ya está cancelada")

            if self._estado == "confirmada":
                raise Exception("No se puede cancelar una reserva ya confirmada")

            self._estado = "cancelada"

        except Exception as e:
            self._registrar_log(f"Error al cancelar: {e}")

    def procesar(self):
        try:
            if self._estado == "cancelada":
                raise Exception("No se puede procesar una reserva cancelada")

            if self._estado == "confirmada":
                raise Exception("La reserva ya fue procesada")

            self._costo = self._servicio.calcular_costo(self._duracion)

        except Exception as e:
            self._registrar_log(f"Error al procesar la reserva: {e}")

        else:
            self._estado = "confirmada"
            print("Reserva procesada correctamente")

        finally:
            print("Proceso de reserva finalizado")

    def mostrar(self):
        print(f"Cliente: {self._cliente}")
        print(f"Servicio: {self._servicio}")
        print(f"Duración: {self._duracion}")
        print(f"Estado: {self._estado}")
        print(f"Costo: {self._costo}")

    def _registrar_log(self, mensaje):
        with open("logs.txt", "a") as archivo:
            archivo.write(mensaje + "\n")
        print(mensaje)