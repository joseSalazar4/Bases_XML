from random import randint, random

import lxml.etree as et

# Se deben generar las siguientes etiquetas:

"""" 
 <TransConsumo id="2" LecturaM3="" descripcion = "" NumFinca = ""> ESCRIBA 
 id 1 es consumo normal
 id 2 es ajuste debito (Reclamo de cliente)
 id 3 ajuste credito (Error del men que hace la lectura)
"""


def buscarNodo(fechaBuscada, root):
    operaciones = root.findall('OperacionDia')
    for operacion in operaciones:
        if operacion.get('fecha') == fechaBuscada:
            return operacion
    print("Algo Fallo")


# Primero son los recibos de medidas normales luego las mods
def modificarArchivo():
    # Se parsea el xml viejo de operaciones
    parser = et.XMLParser(remove_blank_text=True)

    # tree = et.parse('Op_TESTING.xml', parser)

    tree = et.parse('Operaciones.xml', parser)
    root = tree.getroot()

    # Buscamos Fincas y su valor
    listaPropiedadesRecAgua = []
    listaActualMes = []
    listaFechas = []
    mes = "2"

    for operacionDia in root.findall('OperacionDia'):
        fecha = operacionDia.get('fecha')
        # listaFechas.append(fecha)

        for relacion in operacionDia.iter('ConceptoCobroVersusPropiedad'):
            if fecha[6] != mes:
                mes = fecha[6]
                listaPropiedadesRecAgua.append(listaActualMes)
                listaActualMes = []

            if relacion.get('idcobro') == "1":
                propiedad = relacion.get('NumFinca')
                listaActualMes.append([propiedad, fecha, 0])
                #listaPropiedadesRecAgua.append([propiedad, fecha, 0])

    # Febrero
    # Worked fine
    listaPropiedadesRecAgua.pop(0)
    listaPropiedadesRecAgua.pop(0)
    """ 
    for n in range(0, 3):
        for propiedad in listaPropiedadesRecAgua[0]:
            fechaBuscada = propiedad[1]
            listaAux = list(fechaBuscada)
            listaAux[6] = str(int(listaAux[6]) + 1)
            fechaBuscada = "".join(listaAux)
            propiedad[1] = fechaBuscada
            nodoOperacion = buscarNodo(fechaBuscada, root)
            lectura = randint(300, 500)
            propiedad[2] += lectura
            cambioFinca = et.Element("TransConsumo", id="1", LecturaM3=str(propiedad[2]), descripcion="Cobro Mensual",
                                     NumFinca=str(propiedad[0]))
            nodoOperacion.insert(len(nodoOperacion), cambioFinca)
    """
    # Marzo
    for n in range(0, 3):
        for propiedad in listaPropiedadesRecAgua[1]:
            fechaBuscada = propiedad[1]
            listaAux = list(fechaBuscada)
            listaAux[6] = str(int(listaAux[6]) + 1)
            fechaBuscada = "".join(listaAux)
            propiedad[1] = fechaBuscada
            nodoOperacion = buscarNodo(fechaBuscada, root)
            lectura = randint(300, 500)
            propiedad[2] += lectura
            cambioFinca = et.Element("TransConsumo", id="1", LecturaM3=str(propiedad[2]), descripcion="Cobro Mensual",
                                     NumFinca=str(propiedad[0]))
            nodoOperacion.insert(len(nodoOperacion), cambioFinca)

    # Abril
    #for propiedad in listaPropiedadesRecAgua[2]:
     #   print("Tengala Adentro")
        # TODO

        """ 
        Esto genera los cambios en las propiedades 
        !Para Activar los triggers!
        if randint(1, 100) > 95 and fechaDeCambio != fecha:
            numeroFinca = randint(1, len(matrizValoresFinca) - 1)
            fincaElegida = matrizValoresFinca.pop(numeroFinca)
            valorActual = int(float(fincaElegida[1]))
            nuevoValor = valorActual + (randint(int(valorActual / 8), int(valorActual / 4))
                                        * ((-1) ** randint(1, 2)))
            cambioFinca = et.Element("CambioPropiedad", NumFinca=fincaElegida[0], NuevoValor=str(nuevoValor))
            operacionDia.insert(len(operacionDia), cambioFinca)
        """

    # Esto genera el archivo
    s = et.tostring(root, pretty_print=True)
    print(s.decode())

    # Esribir
    tree.write('output.xml', pretty_print=True)


modificarArchivo()
