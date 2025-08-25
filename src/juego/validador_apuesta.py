class ValidarApuesta: 
    @staticmethod
    def es_valida(apuesta_actual:  tuple, apuesta_nueva: tuple, ronda: int, ronda_especial: bool) -> bool:
        
        # Partir ronda con As y sin ser ronda especial
        if apuesta_actual[1] == 'As' and ronda == 1 and not ronda_especial: 
            return False
    
        return True

