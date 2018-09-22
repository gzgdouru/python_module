from xml.etree import ElementTree as ET
from myXml import prettyXml

if __name__ == "__main__":
    a = ET.Element("elem")
    c = ET.SubElement(a, "child1")
    c.set("foo", "bar")
    c.text = "some text"

    d = ET.SubElement(a, "child2")
    b = ET.Element("elem_b")

    root = ET.Element("root")
    root.extend((a, b))
    prettyXml(root)

    tree = ET.ElementTree(root)
    tree.write("demo3.xml")