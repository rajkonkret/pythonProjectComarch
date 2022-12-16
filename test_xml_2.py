from xml.dom import minidom

root = minidom.Document()

xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute('name', 'Geeks for Geeks')
xml.appendChild(productChild)
print(root)
xml_str = root.toprettyxml(indent="\t")
print(xml_str)
save_path_file = "gfg.xml"

with open(save_path_file, 'w') as f:
    f.write(xml_str)
