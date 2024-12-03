import random
import threading
import time

salida = threading.Event()

def corredor(idCorredor):
    print(f"Corredor {idCorredor} en posición, esperando señal de salida...")
    salida.wait()
    time.sleep(random.uniform(1, 3))
    print(f"Corredor {idCorredor} ha llegado a la meta")

def iniciarCarrera():
    print("Señal de salida en 2 segundos...")
    time.sleep(2)
    salida.set()
    print("¡Salida! Los corredores han comenzado.")

corredores = []
for i in range(5):
    t = threading.Thread(target=corredor, args=(i,))
    corredores.append(t)
    t.start()

alarma = threading.Thread(target=iniciarCarrera())
alarma.start()

for t in corredores:
    t.join()

alarma.join()


