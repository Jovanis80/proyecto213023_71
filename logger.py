from datetime import datetime

def registrar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as f:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{fecha}] {mensaje}\n")
