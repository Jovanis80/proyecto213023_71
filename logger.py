import os

def registrar_log(mensaje):
    ruta = os.path.join(os.getcwd(), "logs.txt")
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")
    print(f"[LOG GUARDADO EN]: {ruta}")
    print(mensaje)
