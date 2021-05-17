import random


# ================================================
# Implementación clase abstracta algoritmo genético
# ================================================
# Definir clase abstracta Problema_Genetico
# Propiedades:
# - genes: lista de genes usados en el genotipo de los estados.
# - longitud_individuos: longitud de los cromosomas
# Métodos:
# - decodifica: función de obtiene el fenotipo a partir del genotipo.
# - fitness: función de valoración.
# - muta: mutación de un cromosoma
# - cruza: cruce de un par de cromosomas

# En la definición de clase no se especifica si el problema es
# de maximización o de minimización, esto se hace con el
# parámetro en el algoritmo genético que se implemente.

class Problema_Genetico(object):
    # Constructor
    def __init__(self, genes, fun_decodificar, fun_cruzar, fun_mutar, fun_fitness, longitud_individuos):
        self.genes = genes
        self.fun_decodificar = fun_decodificar
        self.fun_cruzar = fun_cruzar
        self.fun_mutar = fun_mutar
        self.fun_fitness = fun_fitness
        self.longitud_individuos = longitud_individuos

    def decodificar(self, genotipo):
        # Devuelve el fenotipo a partir del genotipo
        fenotipo = self.fun_decodificar(genotipo)
        return fenotipo

    def cruzar(self, cromosoma1, cromosoma2):
        # Devuelve el cruce de un par de cromosomas
        cruce = self.fun_cruzar(cromosoma1, cromosoma2)
        return cruce

    def mutar(self, cromosoma, prob):
        # Devuelve el cromosoma mutado
        mutante = self.fun_mutar(cromosoma, prob)
        return mutante

    # Si se quisiera implementar otro mecanismo de cruza
    # def cruza_loca(self, cromosoma1, cromosoma2, cromosoma3, cromosoma4):
    #    cruce = self.fun_cruza(cromosoma1, cromosoma2, cromosoma3, cromosoma4)
    #    return cruce

    def fitness(self, cromosoma):
        # Función de valoración
        valoracion = self.fun_fitness(cromosoma)
        return valoracion

# Función interpreta lista de 0's y 1's como número natural:

def binario_a_decimal(x):
    return sum(b * (2 ** i) for (i, b) in enumerate(x))

def fun_decodificar(x):
    return [binario_a_decimal(x[::])]

def fun_cruzar(cromosoma1, cromosoma2):
    # Cruza los cromosomas por la mitad
    l1 = len(cromosoma1)
    l2 = len(cromosoma2)
    cruce1 = cromosoma1[0:int(l1 / 2)] + cromosoma2[int(l1 / 2):l2]
    cruce2 = cromosoma2[0:int(l2 / 2)] + cromosoma1[int(l2 / 2):l1]
    return [cruce1, cruce2]
# print(fun_cruzar([1,0,0,0,1,1,0,0,1,0,1],[0,1,1,0,1,0,0,1,1,1]))

def fun_mutar(cromosoma, prob):
    # Elige un elemento al azar del cromosoma y lo modifica con una probabilidad igual a prob
    l = len(cromosoma)
    p = random.randint(0, l - 1)
    if prob >= random.uniform(0, 1):
        cromosoma[p] =  (cromosoma[p] + 1) % 2
        #cromosoma[p] = cromosoma[p]*-1
    return cromosoma

# print(fun_mutar([1,0,0,0,1,1,0,0,1,0,1],0.1))

# Definir una función poblacion_inicial(problema_genetico, tamaño), para
# definir una población inicial de un tamaño dado, para una instancia dada de
# la clase anterior Problema_Genetico

def poblacion_inicial(problema_genetico, tamano_poblacion):
    l = []
    for i in range(tamano_poblacion):
        l.append([random.choice(problema_genetico.genes) for i in range(problema_genetico.longitud_individuos)])
    return l

# Definir una función cruza_padres(problema_genetico, padres), que recibiendo
# una instancia de Problema_Genetico y una población de padres (supondremos
# que hay un número par de padres), obtiene la población resultante de
# cruzarlos de dos en dos (en el orden en que aparecen)

def cruza_padres(problema_genetico, padres):
    l = []
    l1 = len(padres)
    while padres != []:
        l.extend(problema_genetico.cruzar(padres[0], padres[1]))
        padres.pop(0)
        padres.pop(0)
    return l

# Definir una función muta_individuos(problema_genetico, poblacion, prob), que
# recibiendo una instancia de Problema_Genetico, una población y una
# probabilidad de mutación, obtiene la población resultante de aplicar
# operaciones de mutación a cada individuo.

def muta_individuos(problema_genetico, poblacion, prob):
    return [problema_genetico.mutar(individuo, prob) for individuo in poblacion]

# Definir una función
# seleccion_por_torneo(problema_genetico,poblacion,n,k,opt)
# que implementa la selección mediante torneo de n individuos de una
# población.  Esta función recibe como entrada una instancia de
# Problema_Genetico, una población, un número natural n (número de individuos
# a seleccionar) un número natural k (número de participantes en el torneo) y
# un valor opt que puede ser o la función max o la función min (dependiendo de
# si el problema es de maximización o de minimización, resp.).

# INDICACIÓN: Usar random.sample

def seleccion_por_torneo(problema_genetico, poblacion, n, k, opt):
    # Selección por torneo de n individuos de una población. Siendo k el nº de participantes
    # y opt la función max o min.
    seleccionados = []
    for i in range(n):
        participantes = random.sample(poblacion, k)
        seleccionado = opt(participantes, key = problema_genetico.fitness)
        #opt(poblacion, key = problema_genetico.fitness)
        seleccionados.append(seleccionado)
        # poblacion.remove(seleccionado)
    return seleccionados

def nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar):
    padres2 = seleccion_por_torneo(problema_genetico, poblacion, n_directos, k, opt)
    padres1 = seleccion_por_torneo(problema_genetico, poblacion, n_padres , k, opt)
    cruces =  cruza_padres(problema_genetico, padres1)
    generacion = padres2 + cruces
    resultado_mutaciones = muta_individuos(problema_genetico, generacion, prob_mutar)
    return resultado_mutaciones

# La siguiente función algoritmo_genetico_t implementa el primero de los
# algoritmos genéticos (el de selección por torneo)

def algoritmo_genetico_t(problema_genetico, k, opt, ngeneraciones, tamano_poblacion, prop_cruces, prob_mutar):
    poblacion = poblacion_inicial(problema_genetico, tamano_poblacion)
    print("Poblacion Inicial")
    print(poblacion)
    n_padres = round(tamano_poblacion * prop_cruces)
    n_padres = int (n_padres if n_padres % 2 == 0 else n_padres - 1)
    n_directos = tamano_poblacion - n_padres
    for _ in range(ngeneraciones):
        poblacion = nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar)
        print("Nueva población")
        print(poblacion)
        for ind in poblacion:
            if(problema_genetico.fitness(ind) == 0):
                print("la solucion es:")
                print("---------------------------")
                re = ind[::]
                #print(ind)
                print(re[:6])
                print(re[6:12])
                print(re[12:18])
                print(re[18:24])
                print(re[24:30])
                print(re[30:36])
                print("---------------------------")
                break

    mejor_cr = opt(poblacion, key = problema_genetico.fitness)
    mejor = problema_genetico.decodificar(mejor_cr)
    return (mejor, problema_genetico.fitness(mejor_cr))

def fun_fitnnes_ecuacion_ajedrez(cromosoma):
    #Función de valoración de un cromosoma en relacion a resolover la ecuacion
    y = 45460576917
    x1 = binario_a_decimal(cromosoma[::])
    fitnnes = abs(x1-y)
    #print (f"x1:{x1}, fitnnes{fitnnes}")

    return fitnnes

ecua_gen_ajedrez = Problema_Genetico([0, 1], fun_decodificar, fun_cruzar, fun_mutar, fun_fitnnes_ecuacion_ajedrez, 36)
print(algoritmo_genetico_t(ecua_gen_ajedrez, 7, min, 150, 150, 0.4, 0.5))

#ecua_por_ag = Problema_Genetico([0, 1], fun_decodificar, fun_cruzar, fun_mutar, fun_fitnnes_ecuacion, 12)
#ecua_gen2 = Problema_Genetico([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], deco_x2, fun_cruzar, fun_mutar, fun_fitnnes_ecuacion2, 2)

#Prueba resolucion de ecuacino utilizando representacion binaria
#print(algoritmo_genetico_t(ecua_por_ag, 3, min, 50, 50, 0.6, 0.2))

#Prueba resolucion de ecuacino utilizando representacion binaria
#print(algoritmo_genetico_t(ecua_gen2, 3, min, 50, 10, 0.7, 0.1))


