import xml.etree.ElementTree as ET

def parse_node(node_elem):
    """Recursively parse a Freeplane <node>"""
    node = {
        "id": node_elem.attrib.get("ID"),
        "text": node_elem.attrib.get("TEXT", ""),
        "created": node_elem.attrib.get("CREATED"),
        "modified": node_elem.attrib.get("MODIFIED"),
        "children": [],
    }

    for child in node_elem.findall("node"):
        node["children"].append(parse_node(child))

    return node


def parse_freeplane(xml_text: str) -> dict:
    tree = ET.fromstring(xml_text)

    if tree.tag != "map":
        raise ValueError("Invalid Freeplane file")

    root_node_elem = tree.find("node")
    if root_node_elem is None:
        raise ValueError("No root node found")

    root_node = parse_node(root_node_elem)

    return {
        "title": root_node["text"],
        "root": root_node,
    }
