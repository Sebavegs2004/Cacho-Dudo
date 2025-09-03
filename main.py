from src.juego.gestor_partida import GestorPartida

def print_juego():
    print("""
 ________  __        _______                    __           
/        |/  |      /       \\                 /  |          
$$$$$$$$/ $$ |      $$$$$$$  | __    __   ____$$ |  ______  
$$ |__    $$ |      $$ |  $$ |/  |  /  | /    $$ | /      \\ 
$$    |   $$ |      $$ |  $$ |$$ |  $$ |/$$$$$$$ |/$$$$$$  |
$$$$$/    $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
$$ |_____ $$ |      $$ |__$$ |$$ \\__$$ |$$ \\__$$ |$$ \\__$$ |
$$       |$$ |      $$    $$/ $$    $$/ $$    $$ |$$    $$/ 
$$$$$$$$/ $$/       $$$$$$$/   $$$$$$/   $$$$$$$/  $$$$$$/  
                                                            
                                                            
    """)

def espacios():
    print("\n\n\n\n\n\n\n\n\n")

def main() -> None:
    
    # Definir jugadores
    jugadores = int(input("Ingrese la cantidad de jugadores: "))
    
    while jugadores < 2:
        print("La cantidad de jugadores debe ser al menos 2.")
        jugadores = int(input("Ingrese la cantidad de jugadores: "))

    # Crear la partida
    gestor = GestorPartida(jugadores=jugadores)

    # Definir sentido
    sentido = input("Ingrese el sentido de los turnos | [H]orario | [A]ntihorario: ")
    
    while sentido != "H" and sentido != "A":
        espacios()
        print("Sentido no valido.")
        sentido = input("Ingrese el sentido de los turnos | [H]orario | [A]ntihorario: ")
    
    gestor.sentido_turnos(sentido)

    # Bucle principal del juego
    while True:
        # Mostrar un titulo
        espacios()
        print_juego()

        # Iniciar una partida
        gestor.iniciar_partida()
        espacios()
        
        # Apuestas
        while True:
            jugador_actual = gestor.get_jugador_actual()
            tipo_especial = None
            if gestor.jugador_dispone_especial(jugador_actual) and not gestor.procesar_comodin():
                gestor.activar_especial(jugador_actual)
                tipo_especial = input("[A]bierto | [C]errado: ")
                while tipo_especial != "A" and tipo_especial != "C":
                    print("Opción no válida.")
                    tipo_especial = input("[A]bierto | [C]errado: ")

            apuesta = input(f"Jugador {jugador_actual}, ingrese la apuesta: ")
            
            # Procesar apuesta
            while not gestor.procesar_apuesta(apuesta):
                print("Apuesta no valida")
                apuesta = input(f"Jugador {jugador_actual}, ingrese la apuesta: ")
            
            # Avanza al siguiente turno
            espacios()
            gestor.siguiente_turno()
            
            # Posibilidades de juego, dudar, calzar o apostar
            if tipo_especial == 'A':
                gestor.get_dados_contrincantes_actual()
            else:
                gestor.get_dados_jugador_actual()

            posibilidades = input("[A]postar | [D]udar | [C]alzar: ")
            
            while posibilidades != "A" and posibilidades != "D" and posibilidades != "C":
                print("Opción no válida.")
                posibilidades = input("[A]postar | [D]udar | [C]alzar: ")

            # Validar si es duda o calzar
            if posibilidades == "D" or posibilidades == "C":
                gestor.procesar_duda_o_calzo(posibilidades)

                print("\n\n", gestor.eliminar_jugador_sin_dados())
                input("\n\nPresione [Enter] para continuar.")
                break
            
            espacios()
        
            # Si queda un jugador, gana
            if gestor.get_usuarios() == 1:
                print("¡Ganaste!")
                break

if __name__ == "__main__":
    main()