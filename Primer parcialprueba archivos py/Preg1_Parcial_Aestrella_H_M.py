import math
import os
import sys
import time
from queue import PriorityQueue

class Tablero:
    def __init__(self, estados):
        self.estados = estados
        #self.tamano = int(math.sqrt(len(estados)))
        self.alto = 3
        self.ancho = 5
#         longitud = len(estados)
#         div = []
#         raiz = math.sqrt(longitud)
#         if (raiz == int(raiz)):
#             self.alto = int(raiz)
#             self.ancho = int(raiz)
#             print(self.alto)
#             print(self.ancho)
#         else:
#             for divisor in range (1, longitud+1):
#                 if (longitud % divisor) == 0:
#                     div.append(divisor)
#             print (div)
#             if(len(div)>2):
#                 self.alto = div[int(len(div)/2)-1]
#                 self.ancho = div[int(len(div)/2)]
#                 print(self.alto)
#                 print(self.ancho)
#             else:
#                 print ('Número de valores no aceptado')
#                 self.estados = estados

    def ejecutar_accion(self, accion):
        nuevos_estados = self.estados[:]
        indice_vacio = nuevos_estados.index('0')
        if accion == 'I':
            if indice_vacio % self.ancho > 0:
                nuevos_estados[indice_vacio - 1], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[indice_vacio - 1]
        if accion == 'D':
            if indice_vacio % self.ancho < (self.ancho - 1):
                nuevos_estados[indice_vacio + 1], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[indice_vacio + 1]
        if accion == 'S':
            if indice_vacio - self.ancho >= 0:
                nuevos_estados[indice_vacio - self.ancho], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[
                    indice_vacio - self.ancho]
        if accion == 'B':
            if indice_vacio + self.ancho < self.ancho * self.alto:
                nuevos_estados[indice_vacio + self.ancho], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[
                    indice_vacio + self.ancho]
        return Tablero(nuevos_estados)

class Nodo:
    def __init__(self, estado, padre, accion):
        self.estado = estado
        self.padre = padre
        self.accion = accion
#         self.costo = costo
    def __repr__(self):
        return str(self.estado.estados)

    def __eq__(self, otro):
        return self.estado.estados == otro.estado.estados

    def __hash__(self):
        return hash(self.estado)

def get_hijos(padre_Nodo):
    hijos = []
    accions = ['I', 'D', 'S', 'B']
    for accion in accions:
        hijo_estado = padre_Nodo.estado.ejecutar_accion(accion)
        hijo_Nodo = Nodo(hijo_estado, padre_Nodo, accion)
        hijos.append(hijo_Nodo)
    return hijos

def gcalc(Nodo):
    ''' calcula g(n): encuentra el costo del estado actual a partir del estado origen o inicial'''
    contador = 0
    while Nodo.padre is not None:
        Nodo = Nodo.padre
        contador += 1
    return contador

def hamming(estados):
    ''' heuristicaa Hamming: cuenta el numero de posiciones erroneas en diferentes estados'''
    numero_indices_no_ubicados = 0
    objetivo_estados = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '0']
    for i in objetivo_estados:
        if objetivo_estados.index(i) - estados.index(i) != 0 and i != 0:
            numero_indices_no_ubicados += 1
    return numero_indices_no_ubicados


def manhattan_calculate(estados):
    '''heuristica Manhattan: cuenta el numero de cuadros a partir de una ubicacion en relacion a su posicion final'''
    contador = 0
    for i in range(0, 14):
        indice = estados.index(str(i + 1))  # por que el rango inicia en 0
        contador += (abs((i / 5) - (indice / 5)) + abs((i % 3) - (indice % 3)))  # %4 es la columna y /4 es la fila
    return contador

def find_path(Nodo):
    '''Devuelve la ruta inversa de un nodo origen'''
    path = []
    while (Nodo.padre is not None):
        path.append(Nodo.accion)
        Nodo = Nodo.padre
    path.reverse()
    return path

def goal_test():
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '0']

def astar(estado_inicial, estado_objetivo, heuristica):
    '''A* Search Algorithm'''
    start_time = time.time()
    frontera = list()
    contador = 0
    visitado = dict()
    frontera.append(estado_inicial)
    visitado[estado_inicial.estado] = estado_inicial
    while frontera:
        minim = []
        holder = []
        for x in frontera:
            if heuristica == 0:
                minim.append(hamming(x.estado.estados) + gcalc(x))  # This is the F = h + g
            elif heuristica == 1:
                minim.append(manhattan_calculate(x.estado.estados) + gcalc(x))
            holder.append(x)
        m = min(minim)  # finds minimum F value
        estado_inicial = holder[minim.index(m)]

        if estado_inicial.estado.estados == estado_objetivo:  # solution found!
            end_time = time.time()
            print("\n\nSolucion:")
            print("Movimientos: " + str(' '.join(find_path(estado_inicial))))
            print("Numero de nodos expandidos: " + str(contador))
            print("Tiempo empleado: " + str(round((end_time - start_time), 3)))
            # print("Memory Used: " + str(sys.gettamanoof(visitado) + sys.gettamanoof(frontera)) + " kb")
            break

        frontera.pop(frontera.index(estado_inicial))
        for hijo in get_hijos(estado_inicial):
            contador += 1
            s = hijo.estado
            if s not in visitado or gcalc(hijo) < gcalc(visitado[s]):
                visitado[s] = hijo
                frontera.append(hijo)

def main():
    ei = ['0', '7', '2', '4', '5', '1', '12', '3', '8', '9', '6', '11', '13', '14', '10']
    # ei = ['0', '15', '14', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1', '2', '3']

    heuristica = input("Elija la heuristica entre 'H' o 'M' (H es Hamming y M ws Manhattan): ")
    if heuristica == 'H':
        heuristica = 0
    elif heuristica == 'M':
        heuristica = 1

    max_depth = 10
    root = Nodo(Tablero(ei), None, None)
    astar(root, goal_test(), heuristica)
    frontera = []
    frontera.append(root)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()