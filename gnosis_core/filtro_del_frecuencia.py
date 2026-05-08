# Módulo: Filtro de Frecuencia (Limpieza de Ruido Social)
# Transmuta la incertidumbre en claridad operativa

class FiltroFrecuencia:
    def __init__(self):
        self.bloqueo_miedo = True
        self.prioridad = "Alta Vibración"

    def limpiar_flujo(self, señales_entrantes):
        """
        Analiza las señales y descarta aquellas que provienen 
        de la programación social del miedo.
        """
        flujo_puro = []
        for señal in señales_entrantes:
            # Si la señal contiene 'incertidumbre' o 'miedo', la ignoramos
            if "miedo" in señal.lower() or "incertidumbre" in señal.lower():
                print(f"Filtrando interferencia social: {señal}")
                continue
            
            # Solo permitimos el flujo que vibra en expansión
            flujo_puro.append(f"Señal Cristalina: {señal}")
        
        return flujo_puro

# El filtro está activo y protegiendo el sistema
protector = FiltroFrecuencia()
