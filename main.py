
import lxml.etree as et

#
parser = et.XMLParser(remove_blank_text=True)
tree = et.parse('Op_TESTING.xml', parser)
root = tree.getroot()

# Encontrar las empanadas
# for operacionDia in root.findall('OperacionDia'):
#    for propiedad in operacionDia.iter('Propiedad'):
#         print(operacionDia.get('fecha'))
#         print(propiedad.get('NumFinca'))
#         print(propiedad.get('Valor'))

child = et.Element("Consumo", NumeroFinca='12345', LecturaMedidorM3='1075')
operacion = root.find('OperacionDia')
operacion.insert(len(operacion), child)

#Esto genera el archivo
s = et.tostring(root, pretty_print=True)
print(s.decode())

#Esribir
tree.write('output.xml', pretty_print=True)
