from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import registrar_log

def ejecutar_pruebas():

    print("=== INICIO DE PRUEBAS ===")

    # 1. Cliente válido
    try:
        c1 = Cliente("Juan", "juan@gmail.com")
        print("Cliente creado:", c1.get_nombre())
    except Exception as e:
        registrar_log(f"Error cliente válido: {e}")

    # 2. Cliente inválido
    try:
        c2 = Cliente("", "correo")
    except Exception as e:
        registrar_log(f"Error cliente inválido: {e}")

    # 3. Servicio válido
    try:
        s1 = ReservaSala("Sala VIP", 50)
        print("Servicio creado:", s1.nombre)
    except Exception as e:
        registrar_log(f"Error servicio válido: {e}")

    # 4. Servicio inválido
    try:
        s2 = ReservaSala("Sala mala", -10)
    except Exception as e:
        registrar_log(f"Error servicio inválido: {e}")

    # 5. Reserva válida
    try:
        c3 = Cliente("Ana", "ana@gmail.com")
        s3 = Asesoria("Asesoría", 100)
        r1 = Reserva(c3, s3)
        costo = r1.procesar(2)
        print("Costo reserva:", costo)
    except Exception as e:
        registrar_log(f"Error reserva válida: {e}")

    # 6. Reserva con error
    try:
        r2 = Reserva(c3, s3)
        r2.procesar(-5)
    except Exception as e:
        registrar_log(f"Error tiempo inválido: {e}")

    # 7. Otro caso válido
    try:
        c4 = Cliente("Luis", "luis@gmail.com")
        s4 = AlquilerEquipo("Laptop", 30)
        r3 = Reserva(c4, s4)
        print("Costo alquiler:", r3.procesar(3))
    except Exception as e:
        registrar_log(f"Error alquiler válido: {e}")

    # 8. Confirmar reserva
    try:
        r3.confirmar()
        print("Estado:", r3.estado)
    except Exception as e:
        registrar_log(f"Error confirmar: {e}")

    # 9. Cancelar reserva
    try:
        r3.cancelar()
        print("Estado:", r3.estado)
    except Exception as e:
        registrar_log(f"Error cancelar: {e}")

    # 10. Error forzado
    try:
        r4 = Reserva(None, None)
        r4.procesar(1)
    except Exception as e:
        registrar_log(f"Error forzado: {e}")

    print("=== FIN DE PRUEBAS ===")


if __name__ == "__main__":
    ejecutar_pruebas()
