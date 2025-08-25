class ValidarApuesta: 
    @staticmethod
    def es_valida(apuesta_actual:  tuple, apuesta_nueva: tuple, ronda: int, ronda_especial: bool) -> bool:
        
        # Partir ronda con As y sin ser ronda especial
        if apuesta_actual[1] == 'As' and ronda == 1 and not ronda_especial: 
            return False

        # Apuesta con As
        if apuesta_nueva[1] == 'as':
            if (apuesta_actual[0] // 2) + 1 > apuesta_nueva[0]:
                return False
            else: return True

        # Apuesta de as a denominacion
        if apuesta_actual[1] == "as":
            if (apuesta_actual[0] * 2) + 1 > apuesta_nueva[0]:
                return False
            else: return True

        # Apuesta inferior por número sin contar AS
        if apuesta_actual[0] > apuesta_nueva[0]:
            return False
        
        # Apuesta igual por número sin contar AS
        if apuesta_actual[0] == apuesta_nueva[0]:

            # Validar que denominaciones sean validas
            match apuesta_actual[1]:
                case "tonto":
                    if apuesta_nueva[1] in ["tonto"]:
                        return False
                case "tren":
                    if apuesta_nueva[1] in ["tonto", "tren"]:
                        return False
                case "cuadra":
                    if apuesta_nueva[1] in ["tonto", "tren", "cuadra"]:
                        return False
                case "quina":
                    if apuesta_nueva[1] in ["tonto", "tren", "cuadra", "quina"]:
                        return False
                case "sexta":
                    if apuesta_nueva[1] in ["tonto", "tren", "cuadra", "quina", "sexta"]:
                        return False

        return True

