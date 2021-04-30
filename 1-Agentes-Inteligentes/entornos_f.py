#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
entornos_f.py
------------

Entornos y agentes desde una prespectiva funcional

"""

__author__ = 'juliowaissman'

class Entorno:
    """
    Clase abstracta para entornos

    En realidad funciona como un contenedor de funciones
    para hacer una especie de tipo entorno con sus funciones

    """

    def acción_legal(self, s, a):
        """
        @param s: Una tupla con un estado legal del entorno
        @param a: Una accion en el entorno

        @return: True si accion es legal en estado, False en caso contrario

        Por default acepta cualquier acción.

        """
        return True

    def transición(self, s, a):
        """
        @param s: Una tupla con un estado legal del entorno
        @param a: Una accion en el entorno

        @return: (s_n, c_local) una tupla con el nuevo estado y
                 el costo de ir de s a s_n con la acción a

        """
        pass

    def percepción(self, s):
        """
        @param s: Una tupla con un estado legal del entorno
        @return: Tupla con los valores que se perciben del entorno por
                 default el estado completo

        """
        return s


class Agente(object):
    """
    Clase abstracta para un agente que interactua con un
    entorno discreto determinista observable.

    """

    def programa(self, p):
        """
        @param p: Lista con los valores que se perciben de un entorno

        @return: Acción seleccionada por el agente.

        """
        pass


def simulador(entorno, agente, s, T=10, c=0):
    """
    Realiza la simulación de un agente actuando en un entorno de forma genérica

    @param entorno: Un objeto de la clase Entorno
    @param agente: Un objeto de la clase Agente
    @param s: Una tupla con un estado legal del entorno
    @param T: Un int con el número de pasos a simular
    @param c: Un flotante con el costo hasta s 

    @return: [(a_1, s_1, c_1), ..., (a_T, s_T, c_T)] una lista de tripletas con
             la acción, estado y costo total en cada paso de simulación.

    """
    a = agente.programa(entorno.percepción(s))
    if not entorno.acción_legal(a):
        raise ValueError("Error en el agente, ofrece una acción no legal")
    s_n, c_local = entorno.transición(s, a)

    return ([] + [(a, s_n, c + c_local)] if T <= 1 else
            [(a, s_n, c + c_local)] + simulador(entorno, agente, s_n, T - 1, c + c_local))
    
def imprime_simulación(historial, s_0):
    """
    Imprime una secuencia generada por simulador

    @param historial: el resultado de simulador
    @param s_0: estado inicial

    """
    print("\n\nSimulación, iniciando en el estado" + 
            str(s_0) + "\n") 

    print('Paso'.center(10) +
            'Acción'.center(40) +
            'Siguente estado'.center(25) +
            'Costo'.center(15))
    print('_' * (10 + 40 + 25 + 15))

    for (i, (a_i, s_i, c_i)) in enumerate(historial):
        print(str(i).center(10) +
                str(a_i).center(40) +
                str(s_i).center(25) +
                str(c_i).rjust(12))
    print('_' * (10 + 40 + 25 + 15) + '\n\n')

