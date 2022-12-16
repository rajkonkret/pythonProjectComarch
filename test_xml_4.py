import xml.etree.ElementTree as ET


def generate_XML(file_name):
    root = ET.Element("Catalog")

    m1 = ET.Element('mobile')
    root.append(m1)

    b1 = ET.SubElement(m1, 'brand')
    b1.text = "Redmi"

    m2 = ET.Element('mobile')
    root.append(m2)

    b2 = ET.SubElement(m2, 'brand')
    b2.text = "Samsung"

    m3 = ET.Element('mobile')
    root.append(m3)

    b3 = ET.SubElement(m3, 'brand')
    b3.text = "Iphone"

    tree = ET.ElementTree(root)

    with open(file_name, 'wb') as files:
        tree.write(files)


if __name__ == "__main__":
    generate_XML('Catalog.xml')
