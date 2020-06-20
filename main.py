from random import randint, random

import lxml.etree as et

# Se deben generar las siguientes etiquetas:
"""" 
 <TransConsumo id="2" LecturaM3="" descripcion = ""> ESCRIBA 
 id 1 es consumo normal
 id 2 es ajuste debito (Reclamo de cliente)
 id 3 ajuste credito (Error del men que hace la lectura)
"""


def modificarArchivo():
    # Se parsea el xml viejo de operaciones
    parser = et.XMLParser(remove_blank_text=True)
    tree = et.parse('Op_TESTING.xml', parser)
    root = tree.getroot()

    # Buscamos Fincas y su valor
    matrizValoresFinca = []
    listaFechas = []

    for operacionDia in root.findall('OperacionDia'):
        fecha = operacionDia.get('fecha')
        listaFechas.append(fecha)
        for propiedad in operacionDia.iter('Propiedad'):
            valor = propiedad.get('Valor')
            propiedad = propiedad.get('NumFinca')
            matrizValoresFinca.append([propiedad, valor])

            fechaDeCambio = listaFechas[randint(0, len(listaFechas) - 1)]
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
            # if para los recibos

    # Esto genera el archivo
    s = et.tostring(root, pretty_print=True)
    print(s.decode())

    # Esribir
    tree.write('output.xml', pretty_print=True)


modificarArchivo()
