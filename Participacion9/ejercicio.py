from typing import Dict, Any

class AnalizadorEventos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_eventos(self) -> Dict[str, Any]:
        eventos_totales = 0
        eventos_por_tipo = {}
        eventos_por_servidor = {}

        archivo = open("eventos.txt", 'r')
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            if linea.startswith("Tipo de evento:"):
                tipo_evento = linea.split(": ")[1]
                eventos_totales += 1
                if tipo_evento in eventos_por_tipo:
                    eventos_por_tipo[tipo_evento] += 1
                else:
                    eventos_por_tipo[tipo_evento] = 1

            elif linea.startswith("Servidor:"):
                nombre_servidor = linea.split(": ")[1]
                if nombre_servidor in eventos_por_servidor:
                    eventos_por_servidor[nombre_servidor] += 1
                else:
                    eventos_por_servidor[nombre_servidor] = 1

        estadisticas = {
            "Número final de eventos registrados": eventos_totales,
            "Número de eventos por tipo": eventos_por_tipo,
            "Número de eventos por servidor": eventos_por_servidor
        }

        return estadisticas