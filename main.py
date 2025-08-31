from src.juego.gestor_partida import GestorPartida

def main() -> None:
    jugadores = int(input("Ingrese la cantidad de jugadores: "))
    
    while jugadores < 2:
        print("La cantidad de jugadores debe ser al menos 2.")
        jugadores = int(input("Ingrese la cantidad de jugadores: "))

    gestor = GestorPartida(jugadores=jugadores)

    while True:
        gestor.iniciar_partida()
        print("\n\n")
        
        # Apuestas
        while True:
            gestor.get_dados_jugador_actual()
            apuesta = input(f"Jugador {gestor.get_jugador_actual()}, ingrese la apuesta: ")
            
            # Procesar apuesta
            while not gestor.procesar_apuesta(apuesta): 
                print("Apuesta no valida")
                apuesta = input(f"Jugador {gestor.get_jugador_actual()}, ingrese la apuesta: ")

            print("\n\n")
            gestor.siguiente_turno()
            print("\n\n")

            posibilidades = int(input("¿Desea apostar, dudar o calzar? (seleccione 1, 2 o 3 respectivamente): "))
            

            if posibilidades == 2 or posibilidades == 3:
                gestor.procesar_duda_o_calzo(posibilidades)
                print(gestor.eliminar_jugador_sin_dados())
                break

            print("\n\n")
        
        if gestor.get_usuarios() == 1: 
            print("¡Ganaste!")
            break

if __name__ == "__main__":
    main()