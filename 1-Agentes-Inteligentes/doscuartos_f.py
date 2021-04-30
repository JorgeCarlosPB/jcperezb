#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
doscuartos_f.py
----------------

Ejemplo de un entorno muy simple y agentes idem

"""

import entornos_f
from random import choice


__author__ = 'juliowaissman'


class DosCuartos(entornos_f.Entorno):
    """
    Clase para un entorno de dos cuartos. 
    Muy sencilla solo regrupa métodos.

    El estado se define como (robot, A, B)
    donde robot puede tener los valores "A", "B"
    A y B pueden tener los valores "limpio", "sucio"

    Las acciones válidas en el entorno son 
        ("ir_A", "ir_B", "limpiar", "nada").
    
    Todas las acciones son válidas en todos los estados.

    Los sensores es una tupla (robot, limpio?)
    con la ubicación del robot y el estado de limpieza

    """
    def acción_legal(self, acción):
        return acción in ("ir_A", "ir_B", "limpiar", "nada")

    def transición(self, estado, acción):
        robot, a, b = estado

        c_local = 0 if a == b == "limpio" and acción is "nada" else 1

        return ((estado, c_local) if a is "nada" else
                (("A", a, b), c_local) if acción is "ir_A" else
                (("B", a, b), c_local) if acción is "ir_B" else
                ((robot, "limpio", b), c_local) if robot is "A" else
                ((robot, a, "limpio"), c_local))

    def percepción(self, estado):
        return estado[0], estado[" AB".find(estado[0])]


class AgenteAleatorio(entornos_f.Agente):
    """
    Un agente que solo regresa una acción al azar entre las acciones legales

    """
    def __init__(self, acciones):
        self.acciones = acciones

    def programa(self, _):
        return choice(self.acciones)


class AgenteReactivoDoscuartos(entornos_f.Agente):
    """
    Un agente reactivo simple

    """
    def programa(self, percepción):
        robot, situación = percepción
        return ('limpiar' if situación == 'sucio' else
                'ir_A' if robot == 'B' else 'ir_B')


class AgenteReactivoModeloDosCuartos(entornos_f.Agente):
    """
    Un agente reactivo basado en modelo

    """
    def __init__(self):
        """
        Inicializa el modelo interno en el peor de los casos

        """
        self.modelo = ['A', 'sucio', 'sucio']

    def programa(self, percepción):
        robot, situación = percepción

        # Actualiza el modelo interno
        self.modelo[0] = robot
        self.modelo[' AB'.find(robot)] = situación

        # Decide sobre el modelo interno
        a, b = self.modelo[1], self.modelo[2]
        return ('nada' if a == b == 'limpio' else
                'limpiar' if situación == 'sucio' else
                'ir_A' if robot == 'B' else 'ir_B')


def prueba_agente(agente):
    entornos_f.imprime_simulación(
        entornos_f.simulador(
            DosCuartos(),
            agente,
            ["A", "sucio", "sucio"],
            100
        ),
        ["A", "sucio", "sucio"]
    )

def test():
    """
    Prueba del entorno y los agentes

    """
    print("Prueba del entorno con un agente aleatorio")
    prueba_agente(AgenteAleatorio(['ir_A', 'ir_B', 'limpiar', 'nada']))

    print("Prueba del entorno con un agente reactivo")
    prueba_agente(AgenteReactivoDoscuartos())

    print("Prueba del entorno con un agente reactivo con modelo")
    prueba_agente(AgenteReactivoModeloDosCuartos())
    

if __name__ == "__main__":
    test()
