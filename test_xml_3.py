import xml.etree.ElementTree as ET

# tree = ET.parse('dane_xml.xml')
tree = ET.parse('gfg.xml')

root = tree.getroot()
print(root)

print(root[0].attrib)
print(root[0].attrib.values())
print(root[0].attrib.keys())
print(root[0].attrib.items())
print(root[0].attrib.items())
