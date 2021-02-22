
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

# Manejo de la grafica con bokeh
def graficar (x,y):
    grafica = figure(title = 'Camino aleatorio', x_axis_label= 'pasos', y_axis_label = 'Distancia')
    grafica.line(x, y, legend_label = 'Distancia media')
    show(grafica)


def graficar_2(x, y):
    grafica = figure()
    grafica.line(x,y)
    show(grafica)


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    #Ciclo para mover al borracho por el plano cartesiano
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    
    
    return inicio.distancia(campo.obtener_coordenada(borracho))


def caminata_grafica(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    x_arreglo = []
    y_arreglo = []
    x_arreglo.append(0)
    y_arreglo.append(0)
    #Ciclo para mover al borracho por el plano cartesiano
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        x_arreglo.append(campo.obtener_coordenada(borracho).x)
        y_arreglo.append(campo.obtener_coordenada(borracho).y)
    graficar_2(x_arreglo, y_arreglo)


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre = 'Orazio')
    origen = Coordenada(0,0)
    distancias = []
    #Ciclo para hacer cada intento aleatorio por cada cantidad de pasos
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    return distancias


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    #Hacer una grafica del movimiento de un solo borracho
    distancias_media_por_caminata = []
    campo = Campo()
    borracho = tipo_de_borracho(nombre = 'Orazio')
    inicio = Coordenada(0,0)
    campo.anadir_borracho(borracho, inicio)
    distancia = 100000
    caminata_grafica(campo, borracho,distancia)
    #Ciclo para cada cantidad de pasos
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} tuvo una caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Maxima = {distancia_maxima}')
        print(f'minima = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)

# Entry point
if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100
    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
