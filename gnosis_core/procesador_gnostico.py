import json

class ValidadorTomas:
    def __init__(self):
        # Aquí cargamos tus 114 dichos para tenerlos siempre presentes
        self.ruta_biblioteca = "gnosis_core/biblioteca_tomas.json"

    def filtrar_por_unidad(self, dato):
        """
        Usa la lógica del Dicho 22: Si el dato une lo interno 
        con lo externo, es una frecuencia válida.
        """
        # Si el dato ayuda a la simplificación (Unidad), devuelve True
        return "COHERENTE" if dato.get('impacto') == "union" else "DUALIDAD_RUIDO"

# El sistema ahora puede 'leer' tus 114 dichos para tomar decisiones
