import pickle
from datetime import datetime
from typing import List, Union
from pydantic import BaseModel

class Transaccion(BaseModel):
    monto: float
    fecha: str
    descripcion: str
    tipo: str

class RegistroFinanciero:
    def __init__(self, transacciones: List[Transaccion] = []):
        self.transacciones = transacciones

    def agregar_transaccion(self, transaccion: Transaccion):
        self.transacciones.append(transaccion)
        print("Transacción agregada con éxito.")

    def listar_transacciones(self):
        if not self.transacciones:
            print("No hay transacciones para mostrar.")
        else:
            transacciones_ordenadas = sorted(self.transacciones, key=lambda x: x.fecha)
            for t in transacciones_ordenadas:
                print(f"{t.fecha} - {t.descripcion}: {t.monto} ({t.tipo})")

    def calcular_balance(self):
        ingresos = sum(t.monto for t in self.transacciones if t.tipo == 'Ingreso')
        gastos = sum(t.monto for t in self.transacciones if t.tipo == 'Gasto')
        ahorro = ingresos - gastos
        print(f"Ingresos totales: {ingresos}")
        print(f"Gastos totales: {gastos}")
        print(f"Capacidad de ahorro: {ahorro}")

    def guardar_datos(self, archivo: str = 'datos_financieros.pkl'):
        try:
            with open(archivo, 'wb') as f:
                pickle.dump(self.transacciones, f)
            print("Datos guardados exitosamente.")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def cargar_datos(self, archivo: str = 'datos_financieros.pkl'):
        try:
            with open(archivo, 'rb') as f:
                self.transacciones = pickle.load(f)
            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("No se encontró el archivo. Inicializando en un estado vacío.")
        except Exception as e:
            print(f"Error al cargar datos: {e}")

# Ejemplo de uso
registro_financiero = RegistroFinanciero()
registro_financiero.cargar_datos()

while True:
    print("\n1. Agregar Transacción")
    print("2. Listar Transacciones")
    print("3. Calcular Balance")
    print("4. Guardar Datos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        monto = float(input("Ingrese el monto: "))
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        descripcion = input("Ingrese la descripción: ")
        tipo = input("Ingrese el tipo (Ingreso/Gasto): ").capitalize()
        transaccion = Transaccion(monto=monto, fecha=fecha, descripcion=descripcion, tipo=tipo)
        registro_financiero.agregar_transaccion(transaccion)

    elif opcion == '2':
        registro_financiero.listar_transacciones()

    elif opcion == '3':
        registro_financiero.calcular_balance()

    elif opcion == '4':
        registro_financiero.guardar_datos()

    elif opcion == '5':
        break

    else:
        print("Opción no válida. Intente nuevamente.")