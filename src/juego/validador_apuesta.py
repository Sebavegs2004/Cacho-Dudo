class ValidarApuesta: 
    @staticmethod
    def es_valida(apuesta_actual:  tuple, apuesta_nueva: tuple, ronda: int, ronda_especial: bool) -> bool:
        # Apuesta con As en ronda 1 y ronda especial        
        if apuesta_nueva[1] == 'as' and ronda == 1 and ronda_especial:
            return True
        
        # Partir ronda con As y sin ser ronda especial
        if apuesta_nueva[1] == 'as' and ronda == 1 and not ronda_especial: 
            return False
        
        # Apuesta con ases
        if apuesta_nueva[1] == 'as' and apuesta_actual[1] == "as":
            if apuesta_actual[0] < apuesta_nueva[0]:
                return True
            else: return False

        # Apuesta con As
        if apuesta_nueva[1] == 'as' and apuesta_actual[1] != "as":
            if (apuesta_actual[0] // 2) + 1 > apuesta_nueva[0]:
                return False
            else: return True

        # Apuesta de as a denominacion
        if apuesta_actual[1] == "as" and apuesta_nueva[1] != "as":
            if (apuesta_actual[0] * 2) + 1 > apuesta_nueva[0]:
                return False
            else: return True
        
        # Apuesta con ases


        # Apuesta inferior por número sin contar AS
        if apuesta_actual[0] > apuesta_nueva[0]:
            return False

        denominaciones = ["tonto", "tren", "cuadra", "quina", "sexta"]
        
        while True: 
            if apuesta_actual[1] != denominaciones[-1]:
                denominaciones.pop()
            else: break

        # Apuesta igual por número sin contar AS
        if apuesta_actual[0] == apuesta_nueva[0]:

            # Validar que denominaciones sean validas
            if apuesta_nueva[1] in denominaciones:
                return False

        return True

