from xml.etree import ElementTree as ET
from myXml import prettyXml

if __name__ == "__main__":
    tree = ET.ElementTree(file="demo1.xml")
    root = tree.getroot()

    del root[2]

    root[0].set("foo", "bar")
    for elem in root:
        print(elem.tag, elem.attrib)

    prettyXml(root)
    tree.write("demo2.xml")
