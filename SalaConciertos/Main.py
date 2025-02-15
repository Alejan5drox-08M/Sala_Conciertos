import json
import requests  # Necesario para peticiones HTTP

class Sala:
    """
    Clase para gestionar las entradas de una sala de conciertos.
    """

    def __init__(self, grupo_musical: str):
        self.grupo_musical = grupo_musical
        self.entradas_concierto = ["LIBRE"] * 7  # Inicializamos las entradas como 'LIBRE'

    def reservar_entrada(self, nombre: str, posicion_libre: int) -> None:
        """
        Reserva una entrada con el nombre del cliente.
        """
        if not nombre:  # Verificamos si el nombre está vacío
            print("Error: El nombre no puede estar vacío.")
            return
        self.entradas_concierto[posicion_libre] = nombre
        print("Reserva realizada CORRECTAMENTE")

    def comprar_entrada(self, posicion_libre: int) -> None:
        """
        Marca una entrada como vendida en taquilla.
        """
        self.entradas_concierto[posicion_libre] = "VENDIDA TAQUILLA"
        print("Compra realizada CORRECTAMENTE")

    def plaza_libre(self, tipo: int) -> int:
        """
        Devuelve la primera plaza libre según el tipo de entrada:
        1.- Normal (0 a 4)
        2.- Premium (5 y 6)
        """
        if tipo == 1:
            # Buscamos en las plazas normales (0-4)
            return next((i for i in range(5) if self.entradas_concierto[i] == "LIBRE"), -1)
        elif tipo == 2:
            # Buscamos en las plazas premium (5-6)
            return next((i for i in range(5, 7) if self.entradas_concierto[i] == "LIBRE"), -1)
        else:
            print("Opción no válida.")
            return -1

    def inicializar(self) -> None:
        """
        Inicializa todas las entradas como libres.
        """
        self.entradas_concierto = ["LIBRE"] * 7

    def visualizar_sala(self) -> None:
        """
        Muestra el estado actual de las entradas.
        """
        print(f"Entradas actuales: {self.entradas_concierto}")

    def num_plazas_libres(self) -> None:
        """
        Muestra el número de plazas libres, tanto normales como premium.
        """
        # Usamos una función lambda para contar las plazas libres
        contar_libres = lambda inicio, fin: sum(1 for i in range(inicio, fin) if self.entradas_concierto[i] == "LIBRE")
        num_libres_normales = contar_libres(0, 5)  # Contamos las plazas normales
        num_libres_premium = contar_libres(5, 7)  # Contamos las plazas premium
        print(f"Número de plazas libres Normales: {num_libres_normales}")
        print(f"Número de plazas libres Premium: {num_libres_premium}")

    def enviar_json(self) -> None:
        """
        Simula el envío de un JSON con el estado de las entradas.
        """
        data = json.dumps({"grupo_musical": self.grupo_musical, "entradas": self.entradas_concierto})
        print(f"Enviando JSON: {data}")
        # Simulamos una petición HTTP
        try:
            # He utilizado esta página para la petición HTTP ya que es una herramienta muy sencilla y fácil de usar que está diseñada específicamente para probar y depurar solicitudes HTTP y además permite ver la respuesta que devuelve
            response = requests.post("https://httpbin.org/post", data=data,)
            print(f"Respuesta del servidor: {response.text}")
        except Exception as e:
            print(f"Error enviando la petición: {e}")

class Main:
    """
    Clase para gestionar el flujo principal del programa.
    """

    def main(self):
        opcion = -1
        gestion1 = Sala("Jurasico Parchis")
        gestion1.inicializar()

        try:
            while opcion != 0:
                # Menú de opciones
                print("MENU DE OPCIONES:" +
                      "\n1.- Reserva Entrada" +
                      "\n2.- Comprar entrada Taquilla" +
                      "\n3.- Visualizar Sala" +
                      "\n4.- Entradas Libres" +
                      "\n5.- Enviar datos en JSON" +
                      "\n0.- Salir")

                # Leer opción del usuario
                opcion = int(input("Ingrese la opción elegida: "))

                # Ejemplo de match-case en Python (equivalente a switch-case en Java)
                match opcion:
                    case 1:
                        tipo = int(input("Introduzca tipo de entrada 1.- Normal  2.- Premium: "))
                        posicion_libre = gestion1.plaza_libre(tipo)
                        if posicion_libre != -1:
                            nombre = input("Introduzca su nombre: ")
                            gestion1.reservar_entrada(nombre, posicion_libre)
                        else:
                            print("No existen entradas disponibles del tipo deseado")

                    case 2:
                        tipo = int(input("Introduzca tipo de entrada 1.- Normal  2.- Premium: "))
                        posicion_libre = gestion1.plaza_libre(tipo)
                        if posicion_libre != -1:
                            gestion1.comprar_entrada(posicion_libre)
                        else:
                            print("No existen entradas disponibles del tipo deseado")

                    case 3:
                        gestion1.visualizar_sala()

                    case 4:
                        gestion1.num_plazas_libres()

                    case 5:
                        gestion1.enviar_json()

                    case 0:
                        print("¡Adiós!")

                    case _:
                        print("Número no reconocido")

                print("\n")  # Salto de línea
            print("Hasta pronto")

        except Exception as e:
            print(f"¡Uoop! Error: {e}")


# Simula la ejecución principal en Python
if __name__ == "__main__":
    app = Main()
    app.main()
