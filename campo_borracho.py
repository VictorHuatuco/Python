
class campo:
    def __init__(self):
        self.coordenadas_de_borracho = {}

    def añadir_borracho(self, camino_borracho, coordenada_borracho):
        self.coordenadas_de_borracho[camino_borracho] = coordenada_borracho

    def mover_borracho(self, camino_borracho):
        delta_x, delta_y = camino_borracho.camina()
        coordenada_actual = self.coordenadas_de_borracho[camino_borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borracho[camino_borracho] = nueva_coordenada

    def obtener_coordenada(self, camino_borracho):
        return self.coordenadas_de_borracho[borracho]
