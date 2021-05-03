# Búsqueda Coste Uniforme - Uniform Cost Search
from Nodos import Nodo

def Comparar(nodo):
    return nodo.get_costo()

def busqueda_BCU(conecciones, estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodo_raiz.set_costo(0)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        # Ordenar lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key=Comparar)
        nodo_actual = nodos_frontera[0]
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo_actual.get_estado() == solucion:
            # Solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # Expandir nodos hijo (ciudades con conexion)
            datos_nodo = nodo_actual.get_estado()
            lista_hijos = []
            for achild in conecciones[datos_nodo]:
                hijo = Nodo(achild)
                costo = conecciones[datos_nodo][achild]
                hijo.set_costo(nodo_actual.get_costo() + costo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # Si está en la lista lo sustituimos con el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.equal(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
            nodo_actual.set_hijo(lista_hijos)


if __name__ == "__main__":
    conecciones = {
        #Con un total de "191" nodos o provicincias y comunidades en
        # todo el mapa la busqueda Costo uniforme soporta más de 191 nodos
        #Mapa de carreteras de Bolivia por departamentos
        #PANDO = 9
        'COBIJA':{'Zofra': 14},
        'Zofra':{'COBIJA':14, 'Nareuda': 41, 'Porvenir': 17},
        'Nareuda':{'Zofra': 41, 'Extrema': 33},
        'Extrema':{'Nareuda': 33},
        'Porvenir':{'Zofra': 17, 'Chive':153, 'Puerto Rico':135},
        'Chive':{'Porvenir':153, 'Ixiamas':226},
        'Puerto Rico':{'Porvenir':135, 'El sena':83},
        'El sena':{'Puerto Rico':83,'Nueva Esperanza':72},
        'Nueva Esperanza':{'El sena':72, 'El Choro':48},

        #BENI = 23
        'El Choro':{'Nueva Esperanza':48, 'Riberalta':71, 'Australia':169},
        'Riberalta':{'El Choro':71, 'Guayaramerín':84},
        'Guayaramerín':{'Riberalta':84, 'La Moroña':327},
        'La Moroña':{'Guayaramerín':327, 'Puerto Ustarez':75, 'San Ramón Beni':54},
        'Puerto Ustarez':{'La Moroña':75},
        'San Ramón Beni':{'La Moroña':54, 'San Xavier':184},
        'San Xavier':{'San Ramón Beni':184, 'TRINIDAD':26},
        'TRINIDAD':{'San Xavier':26, 'Pto. Ganadero':13, 'Casarabe':52},
        'Pto. Ganadero':{'TRINIDAD':13, 'Pto. Varador':6},
        'Casarabe':{'TRINIDAD':52, 'San Pablo':85},
        'San Pablo':{'Casarabe':85, 'Ascención de Guarayos':112},
        'Pto. Varador': {'Pto. Ganadero': 6,'Fatima':35},
        'Fatima':{'Pto. Varador':35, 'San Ignacio de Moxos':36},
        'San Ignacio de Moxos':{'Fatima':36, 'Monte Grande del Apere':76, 'San Borja':134},
        'Monte Grande del Apere':{'San Ignacio de Moxos':76},
        'San Borja':{'San Ignacio de Moxos':134, 'Yucumo':51},
        'Yucumo':{'San Borja':51, 'Quiquibey':39, 'Rurrenabaque':101},
        'Rurrenabaque':{'Yucumo':101, 'Santa Rosa':96, 'Tumupasa':53},
        'Santa Rosa':{'Rurrenabaque':96, 'Australia':169},
        'Australia':{'El Choro':169, 'Santa Rosa':169},
        'Quiquibey':{'Yucumo':39, 'Guanay':90},
        'Puerto Villazon':{'Santa Rosa de la Roca':355},
        'San Antonio': {'Isinuta': 62},

        #SANTA CRUZ = 47
        'Ascención de Guarayos':{'San Pablo':112, 'San Ramón':119},
        'San Ramón':{'Ascención de Guarayos':119, 'Río Uruguaito':142, 'Los Troncos':56},
        'Río Uruguaito':{'San Ramón':142, 'Santa Rosa de la Roca':49},
        'Santa Rosa de la Roca':{'Puerto Villazon':355, 'Río Uruguaito':49, 'San Ignacio de Velasco':82},
        'San Ignacio de Velasco':{'Santa Rosa de la Roca':82, 'San Matias':308, 'San Miguel':36},
        'San Matias':{'San Ignacio de Velasco':308},
        'San Miguel':{'San Ignacio de Velasco':36, 'San José de Chiquitos':168, 'Cuatro Cañadas':230},
        'San José de Chiquitos':{'San Miguel':168, 'Roboré':128, 'Hito Palmar':228, 'Quimome':49},
        'Hito Palmar':{'San José de Chiquitos':228},
        'Roboré':{'San José de Chiquitos':128, 'El Carmen':138},
        'El Carmen':{'Roboré':138, 'Puerto Suarez':89},
        'Puerto Suarez':{'El Carmen':89, 'Arroyo Concepción':10, 'Puerto Busch':138},
        'Arroyo Concepción':{'Puerto Suarez':10},
        'Puerto Busch':{'Puerto Suarez':138},
        'Quimome':{'San José de Chiquitos':49, 'El Tinto':37},
        'El Tinto':{'Quimome':37, 'Paraiso':125},
        'Paraiso':{'El Tinto':37, 'Cuatro Cañadas':38, 'Cotoca':41},
        'Cuatro Cañadas':{'Paraiso':38, 'San Miguel':230, 'Los Troncos':26},
        'Los Troncos':{'San Ramón':56, 'Cuatro Cañadas':26, 'Okinawa':34},
        'Cotoca':{'Paraiso':41, 'SANTA CRUZ':20},
        'Okinawa':{'Los Troncos':34, 'Guabirá':41},
        'Guabirá':{'Okinawa':41, 'Saavedra':12, 'Montero':4, 'Yapacaní':67},
        'Saavedra':{'Guabirá':12, 'Chané':29, 'Rosario':32},
        'Chané':{'Saavedra':29, 'Aguaices':15,},
        'Rosario':{'Saavedra':32, 'Aguaices':12, 'La Enconada':66},
        'Aguaices':{'Rosario':12, 'Chané':15, 'Colonia Piraí':74},
        'Colonia Piraí':{'Aguaices':74},
        'La Enconada':{'Rosario':66, 'Yapacaní':48},
        'Yapacaní':{'La Enconada':48, 'Guabirá':67, 'Ivirgarzama':64},
        'Montero':{'Guabirá':4, 'Warnes':21},
        'Warnes':{'Montero':21, 'SANTA CRUZ':31},
        'SANTA CRUZ':{'Warnes':31, 'Cotoca':20, 'La Guardia':20},
        'La Guardia':{'SANTA CRUZ':20, 'Samaipata':99, 'Abapo':133},
        'Abapo':{'El Espino':38, 'Ipita':57},
        'El Espino':{'Abapo':38, 'Boyuibe':192},
        'Ipita':{'Abapo':57 ,'Cruce Ipati':51, 'Guadalupe':181},
        'Cruce Ipati':{'Ipita':51, 'Boyuibe':94, 'Muyupampa':46},
        'Boyuibe':{'Cruce Ipati':94, 'El Espino':192, 'Hito Villazón':127, 'Villamontes':98},
        'Hito Villazón':{'Boyuibe':127},
        'Guadalupe':{'Ipita':181, 'Vallegrande':6, 'Pte. Santa Rosa':76},
        'Pte. Santa Rosa':{'Guadalupe':76},
        'Vallegrande':{'Guadalupe':6, 'Mataral':53},
        'Samaipata':{'La Guardia':99, 'Mataral':67},
        'Mataral':{'Samaipata':67, 'Vallegrande':53, 'La Palizada':32},
        'La Palizada':{'Mataral':32, 'Comarapa':21, 'Pte. Taperas':42},
        'Comarapa':{'La Palizada':21, 'Epizana':131},
        'Pte. Taperas':{'La Palizada':42, 'Aiquile':88},

        #COCHABAMBA = 17
        'Ivirgarzama':{'Yapacaní':64, 'Puerto Villarroel':26, 'Villa Tunari':60},
        'Puerto Villarroel':{'Ivirgarzama':26},
        'Villa Tunari':{'Ivirgarzama':60, 'Isinuta':47, 'Colomi':114},
        'Isinuta':{'Villa Tunari':47, 'San Antonio':62},
        'Colomi':{'Villa Tunari': 114, 'COCHABAMBA':33},
        'Aiquile':{'Pte. Taperas':88, 'Pte Arce':48, 'Mizque':42},
        'Mizque':{'Aiquile':42, 'Cruce Vacas':79},
        'Cruce Vacas':{'Mizque':79, 'Paracaya':29},
        'Paracaya':{'Cruce Vacas':29, 'Epizana':85, 'COCHABAMBA':46},
        'Epizana':{'Paracaya':85, 'Comarapa':131},
        'COCHABAMBA':{'Colomi':33, 'Paracaya':46, 'Vinto':28, 'Toro toro':112},
        'Vinto':{'COCHABAMBA':28, 'Suticollo':8, 'Pte Sacambaya':180},
        'Suticollo':{'Vinto':8, 'Parotani':12},
        'Parotani':{'Suticollo':12, 'Confital':79},
        'Confital':{'Parotani':79, 'Caracollo':72},
        'Pte Sacambaya':{'Vinto':180, 'Chulumani':203},
        'Pte Arce':{'Aiquile':48, 'Pte Sacramento':52},

        #CHUQUISACA = 9
        'Pte Sacramento':{'Pte Arce':52, 'SUCRE':35},
        'SUCRE':{'Pte Sacramento':35, 'Ravelo':45, 'Pte Mendez':43, 'Tarabuco':61},
        'Pte Mendez':{'SUCRE':43, 'POTOSÍ':107},
        'Tarabuco':{'SUCRE':61, 'Zudañez':41},
        'Zudañez':{'Tarabuco':41, 'Padilla':69},
        'Padilla':{'Zudañez':69, 'El salto':49},
        'El salto':{'Padilla':49, 'Monteagudo':69},
        'Monteagudo':{'El salto':69, 'Muyupampa':49},
        'Muyupampa':{'Monteagudo':49, 'Cruce Ipati':46},

        #TARIJA = 23
        'Villamontes':{'Boyuibe':98, 'Palo Marcado':46, 'Palos Blancos':70, 'Campo Pajoso':77},
        'Palo Marcado':{'Villamontes':46, 'Hito BR-94':70},
        'Hito BR-94':{'Palo Marcado':70},
        'Campo Pajoso':{'Villamontes':77, 'Yacuiba':11, 'Carapari':19},
        'Yacuiba':{'Campo Pajoso':11, 'San José de Pocitos':7},
        'San José de Pocitos':{'Yacuiba':7},
        'Carapari':{'Campo Pajoso':19, 'Sidras':62, 'Palos Blancos':63},
        'Sidras':{'Carapari':62},
        'Palos Blancos':{'Carapari':63, 'Villamontes':70, 'Entre Ríos':75},
        'Entre Ríos':{'Palos Blancos':75, 'Canaletas':41},
        'Canaletas':{'Entre Ríos':41, 'TARIJA':58},
        'TARIJA':{'Canaletas':58, 'Cr Concepción':9, 'Cr Norte':19},
        'Cr Concepción':{'TARIJA':9, 'Padcaya':34, 'Canas':46},
        'Padcaya':{'Cr Concepción':34, 'Bermejo':143, 'Cr Rosillas':7},
        'Bermejo':{'Padcaya':143},
        'Cr Rosillas':{'Padcaya':7, 'Canas':9, 'Mecoya':30},
        'Canas':{'Cr Concepción':46, 'Mecoya':30, 'Villazón':127},
        'Mecoya':{'Canas':30, 'Cr Rosillas':30, 'Mecoyita':4},
        'Mecoyita':{'Mecoya':4},
        'Cr Norte':{'TARIJA':19, 'San Lorencito':27, 'Iscayachi':41},
        'Iscayachi':{'Cr Norte':41, 'San Lorencito':11},
        'San Lorencito':{'Iscayachi':11, 'Cr Norte':27, 'El Puente':46},
        'El Puente':{'Lecori':140, 'Hornillos':96, 'San Lorencito':46},

        #POTOSÍ = 16
        'Toro toro':{'COCHABAMBA':112},
        'Villazón': {'Canas': 127, 'Tupiza': 91},
        'Tupiza':{'Villazón':91, 'Hornillos':16, 'Atocha':102},
        'Hornillos':{'Tupiza':16, 'El Puente':96, 'Santiago de Cotagaita':63},
        'Atocha':{'Tupiza':102, 'Uyuni':102},
        'Uyuni':{'Atocha':102, 'Hito Lx':257, 'POTOSÍ':203, 'Condo K':168},
        'Hito Lx':{'Uyuni':257},
        'POTOSÍ':{'Uyuni':203, 'Khucho Ingenio':39, 'Pte Mendez':107, 'Ventilla':102},
        'Khucho Ingenio':{'POTOSÍ':39, 'Lecori':70, 'Tumusla':89},
        'Lecori':{'Khucho Ingenio':70,'El Puente':140},
        'Tumusla':{'Khucho Ingenio':89, 'Santiago de Cotagaita':40},
        'Santiago de Cotagaita':{'Tumusla':40, 'Hornillos':63},
        'Ravelo':{'SUCRE':45, 'Lluchu':62},
        'Lluchu':{'Ravelo':62, 'Chapapuco':63},
        'Chapapuco':{'Lluchu':63, 'Llallagua':64},
        'Llallagua':{'Chapapuco':64, 'Huanuni':42},

        #ORURO = 19
        'Condo K':{'Uyuni':168, 'Challapata':18},
        'Challapata':{'Condo K':18, 'Ventilla':91, 'Machacamarquita':92},
        'Ventilla':{'POTOSÍ':102, 'Challapata':91},
        'Machacamarquita':{'Challapata':92, 'Huanuni':22, 'ORURO':18},
        'Huanuni':{'Llallagua':42, 'Machacamarquita':22},
        'ORURO':{'Machacamarquita':18, 'Ocotavi':36, 'Toledo':36, 'La Joya':50, 'Caracollo':30},
        'Toledo':{'ORURO':36, 'Ancaravi':56},
        'Ancaravi':{'Toledo':56, 'Huachacalla':70, 'Turco':56},
        'Huachacalla':{'Ancaravi':70, 'Pisiga':70},
        'Pisiga':{'Huachacalla':70},
        'Turco':{'Ancaravi':56, 'Hito XVIII':80},
        'Hito XVIII':{'Turco':80, 'Patacamaya':188},
        'La Joya':{'ORURO':50, 'Chuquichambi':38},
        'Chuquichambi':{'La Joya':38, 'Totora':35},
        'Totora':{'Chuquichambi':35, 'Charagua de Carangas':28},
        'Charagua de Carangas':{'Totora':28},
        'Caracollo':{'ORURO':30, 'Patacamaya':88, 'Ocotavi':17, 'Colquiri':35, 'Confital':72},
        'Colquiri':{'Caracollo':35},
        'Ocotavi':{'ORURO':36, 'Caracollo':17},

        #LA PAZ = 28
        'Patacamaya':{'Hito XVIII':188, 'Caracollo':88, 'Nazacara':105, 'LA PAZ':81},
        'Nazacara':{'Patacamaya':105, 'San Andrés de Machaca':25, 'Central Chama':27},
        'San Andrés de Machaca':{'Nazacara':25, 'Santiago de Machaca':32},
        'Santiago de Machaca':{'San Andrés de Machaca':32, 'Hito IV':50},
        'Hito IV':{'Santiago de Machaca':50},
        'Central Chama':{'Nazacara':27, 'Capiri':13},
        'Capiri':{'LA PAZ':13, 'Central Chama':13},
        'LA PAZ':{'Capiri':13, 'Botijlaja':29, 'Patacamaya':81,'La cumbre':22, 'Desaguadero':95, 'Huarina':56},
        'Botijlaja':{'LA PAZ':29, 'Charaña':157},
        'Charaña':{'Botijlaja':157},
        'Desaguadero':{'LA PAZ':95},
        'La cumbre':{'LA PAZ':22, 'Unduavi':25},
        'Unduavi':{'La cumbre':25, 'Pte Villa':49, 'Santa Barbara':50},
        'Pte Villa':{'Unduavi':49, 'Chulumani':24, 'Santa Barbara':59},
        'Chulumani':{'Pte Villa':24, 'Pte Sacambaya':203},
        'Santa Barbara':{'Unduavi':50, 'Pte Villa':59, 'Quiquibey':173},
        'Huarina':{'LA PAZ':56, 'Achacachi':18, 'Tiquina':38},
        'Tiquina':{'Huarina':38, 'Copacabana':38},
        'Copacabana':{'Tiquina':38, 'Kasani':9},
        'Kasani':{'Copacabana':9},
        'Achacachi':{'Huarina':18, 'Escoma':75},
        'Escoma':{'Achacachi':75, 'Charazani':87},
        'Charazani':{'Escoma':87, 'Apolo':142},
        'Apolo':{'Charazani':142, 'Mapiri':123, 'Tumupasa':125},
        'Tumupasa':{'Apolo':125, 'Ixiamas':62, 'Rurrenabaque':53},
        'Ixiamas':{'Tumupasa':62, 'Chive':226},
        'Mapiri':{'Apolo':123, 'Guanay':99},
        'Guanay':{'Mapiri':99, 'Quiquibey':90}

    }
    estado_inicial = 'COBIJA'
    solucion = 'Villazón'
    nodo_solucion = busqueda_BCU(conecciones, estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_estado())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Costo: %s" % str(nodo_solucion.get_costo()))
