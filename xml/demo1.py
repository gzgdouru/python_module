from xml.etree import ElementTree as ET

if __name__ == "__main__":
    tree = ET.ElementTree(file="demo1.xml")
    # root = tree.getroot()
    # for child in root:
    #     print(child.tag, child.attrib, repr(child.text))

    # for elem in tree.iter():
    #     print(elem.tag, elem.attrib)

    # for elem in tree.iter(tag="sub-branch"):
    #     print(elem.tag, elem.attrib)

    # for elem in tree.iterfind('branch/sub-branch'):
    #     print(elem.tag, elem.attrib)

    for elem in tree.iterfind('branch[@name="release01"]'):
        print(elem.tag, elem.attrib)