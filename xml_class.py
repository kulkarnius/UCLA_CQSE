

import xml.etree.ElementTree as ET 
import os
import itertool as it


def createSubDirectory(subDirectoryName):
    currentPath = os.getcwd()
    os.mkdir(currentPath + '/{}'.format(subDirectoryName))

class xml_parser:
    def __init__(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    def getValues(self,valueName):
        return [float(elem.get("value")) for elem in self.root.findall(".//{})".format(valueName))]
    
    def setValue(self, targetValuePath, value):
        self.root.find('.//{}'.format(targetValuePath)).set('value', str(value))

    def getParent(self, valueName):
        return self.root.find(".//{}..)".format(valueName))

    




    

        
