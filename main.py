from cliente import Cliente
from servicios_derivados import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import registrar_log


def ejecutar_pruebas():

    # Prueba válida
    try:
        c1 = Cliente("Javier Lopez", "javier@gmail.com")
        s1 = ReservaSala("Sala VIP", 100)
        r1 = Reserva(c1, s1, 2)
        r1.procesar(0.1)
        r1.mostrar()
    except Exception as e:
        registrar_log(f"Error en prueba válida: {e}")

    # Cliente inválido
    try:
        c2 = Cliente("Ana", "correo")
    except Exception as e:
        registrar_log(f"Error cliente inválido: {e}")

    # Servicio inválido
    try:
        s2 = ReservaSala("", -50)
    except Exception as e:
        registrar_log(f"Error servicio inválido: {e}")

    # Reserva inválida
    try:
        r2 = Reserva(None, None, -1)
    except Exception as e:
        registrar_log(f"Error reserva inválida: {e}")

    # Prueba adicional 1: doble confirmación
    try:
        c3 = Cliente("Carlos Perez", "carlos@gmail.com")
        s3 = AlquilerEquipo("Computador", 50)
        r3 = Reserva(c3, s3, 2)
        r3.confirmar()
        r3.confirmar()
    except Exception as e:
        registrar_log(f"Error doble confirmación: {e}")

    # Prueba adicional 2: procesar cancelada
    try:
        c4 = Cliente("Maria Lopez", "maria@gmail.com")
        s4 = Asesoria("Consultoría", 200)
        r4 = Reserva(c4, s4, 1)
        r4.cancelar()
        r4.procesar()
    except Exception as e:
        registrar_log(f"Error procesar cancelada: {e}")

    # Prueba adicional 3: duración inválida
    try:
        c5 = Cliente("Pedro Gomez", "pedro@gmail.com")
        s5 = ReservaSala("Sala básica", 80)
        r5 = Reserva(c5, s5, 0)
    except Exception as e:
        registrar_log(f"Error duración inválida: {e}")

    # Prueba adicional 4: servicio diferente
    try:
        c6 = Cliente("Laura Diaz", "laura@gmail.com")
        s6 = Asesoria("Asesoría técnica", 150)
        r6 = Reserva(c6, s6, 3)
        r6.procesar()
        r6.mostrar()
    except Exception as e:
        registrar_log(f"Error servicio asesoría: {e}")

    # Prueba adicional 5: cancelar dos veces
    try:
        c7 = Cliente("Andres Ruiz", "andres@gmail.com")
        s7 = AlquilerEquipo("Proyector", 60)
        r7 = Reserva(c7, s7, 2)
        r7.cancelar()
        r7.cancelar()
    except Exception as e:
        registrar_log(f"Error doble cancelación: {e}")


if __name__ == "__main__":
    ejecutar_pruebas()
    

