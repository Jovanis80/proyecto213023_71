from servicio import Servicio
from excepciones import ServicioError

class ReservaSala(Servicio):
    def __init__(self, nombre, tarifa_base):
        # Heredamos exactamente los atributos que pide servicio.py
        super().__init__(nombre, tarifa_base)

    def calcular_costo(self, duracion, descuento=0):
        # Cumplimos con la firma obligatoria de la clase abstracta
        if duracion <= 0:
            raise ServicioError("La duración de la reserva de sala debe ser mayor a cero.")
        
        costo = self.tarifa_base * duracion
        costo -= costo * descuento
        return round(costo, 2)

    def descripcion(self):
        # Reemplaza al 'mostrar_detalles' para coincidir con la clase abstracta
        return f"[SALA] {self.nombre} - Tarifa/hora: ${self.tarifa_base}"


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, tarifa_base):
        super().__init__(nombre, tarifa_base)

    # Añadimos un parámetro opcional para demostrar sobrecarga/polimorfismo
    def calcular_costo(self, duracion, descuento=0, seguro_adicional=False):
        if duracion <= 0:
            raise ServicioError("Los días de alquiler deben ser mayores a cero.")
        
        costo = self.tarifa_base * duracion
        if seguro_adicional:
            costo += 50  # Tarifa fija de seguro
            
        costo -= costo * descuento
        return round(costo, 2)

    def descripcion(self):
        return f"[EQUIPO] {self.nombre} - Tarifa/día: ${self.tarifa_base}"


class Asesoria(Servicio):
    def __init__(self, nombre, tarifa_base):
        super().__init__(nombre, tarifa_base)

    # Añadimos un parámetro opcional de urgencia
    def calcular_costo(self, duracion, descuento=0, tarifa_urgencia=False):
        if duracion <= 0:
            raise ServicioError("Las horas de asesoría deben ser mayores a cero.")
        
        costo = self.tarifa_base * duracion
        if tarifa_urgencia:
            costo *= 1.5  # Recargo del 50%
            
        costo -= costo * descuento
        return round(costo, 2)

    def descripcion(self):
        return f"[ASESORÍA] {self.nombre} - Tarifa/hora: ${self.tarifa_base}"