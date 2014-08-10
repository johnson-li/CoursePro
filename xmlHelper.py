__author__ = 'johnson'

import xml.etree.ElementTree


class XmlHelper:

    elementRoot = ''

    def __init__(self, xml_src):
        self.xmlSrc = xml_src
        self.read_file()

    def read_file(self):
        element_tree = xml.etree.ElementTree.parse(self.xmlSrc)
        self.elementRoot = element_tree.getroot()

    def get_value(self, key):
        return self.elementRoot.find(key).attrib['value']