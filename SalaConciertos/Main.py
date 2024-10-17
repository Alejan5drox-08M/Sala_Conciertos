from SalaConciertos.Sala import Sala


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
