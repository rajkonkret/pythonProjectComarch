from xml.dom import minidom

DOMTree = minidom.parse('dane_xml.xml')
print(DOMTree.toxml())
cNodes = DOMTree.childNodes
print(cNodes)
print(cNodes[0])
print(cNodes[0].getElementsByTagName("osoba"))
print(cNodes[0].getElementsByTagName("osoba")[0])
name = cNodes[0].getElementsByTagName("osoba")[0]
print(cNodes[0].getElementsByTagName("osoba")[0].getElementsByTagName('imie'))
print(cNodes[0].getElementsByTagName("osoba")[0])
print(cNodes[0].getElementsByTagName("osoba")[0].toxml())
